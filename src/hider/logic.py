from __future__ import annotations

import logging
from typing import Any, Final, Literal, override

from anki.cards import Card
from anki.collection import Collection
from aqt import mw
from aqt.operations import QueryOp
from aqt.overview import Overview
from aqt.qt import (
    QWIDGETSIZE_MAX,
    QAction,
    QApplication,
    QCoreApplication,
    QEvent,
    QGuiApplication,
    QObject,
    Qt,
    QTimer,
    QWidget,
)
from aqt.reviewer import Reviewer, ReviewerBottomBar
from aqt.utils import tooltip
from aqt.webview import WebContent

from . import constants
from .settings import HiderConfig, load_config
from .strings import tr

_logger: Final[logging.Logger] = logging.getLogger(constants.PACKAGE_NAME)

Ease = Literal[1, 2, 3, 4]
EaseTuple = tuple[bool, Ease]


def _restore_cursor() -> None:
    while QGuiApplication.overrideCursor() is not None:
        QGuiApplication.restoreOverrideCursor()


def _widget(attr_name: str) -> QWidget | None:
    widget: object = getattr(mw, attr_name, None)
    return widget if isinstance(widget, QWidget) else None


def _eval_js(widget: QWidget, js: str) -> None:
    # toolbarWeb/bottomWeb son AnkiWebView; eval encola el JS hasta que la pagina
    # termina de cargar, asi que es seguro llamarlo en mitad de una transicion.
    eval_fn = getattr(widget, "eval", None)
    if callable(eval_fn):
        eval_fn(js)


class CursorHider(QObject):
    __slots__ = ("_timer", "_idle_ms", "_running")

    def __init__(self, idle_ms: int, parent: QObject | None = None) -> None:
        super().__init__(parent)
        self._idle_ms: int = idle_ms
        self._running: bool = False
        self._timer = QTimer(self)
        self._timer.setSingleShot(True)
        self._timer.timeout.connect(self._on_idle)

    def set_idle_ms(self, idle_ms: int) -> None:
        self._idle_ms = idle_ms
        if self._running:
            self._timer.start(self._idle_ms)

    def activate(self) -> None:
        if self._running:
            return
        app: QCoreApplication | None = QApplication.instance()
        if app is None:
            return
        app.installEventFilter(self)
        self._running = True
        self._timer.start(self._idle_ms)

    def deactivate(self) -> None:
        self._timer.stop()
        app: QCoreApplication | None = QApplication.instance()
        if app is not None and self._running:
            app.removeEventFilter(self)
        self._running = False
        _restore_cursor()

    @override
    def eventFilter(self, watched: QObject | None, event: QEvent | None) -> bool:
        if event is not None and event.type() in constants.MOUSE_EVENT_TYPES:
            _restore_cursor()
            self._timer.start(self._idle_ms)
        return False

    @staticmethod
    def _on_idle() -> None:
        if QGuiApplication.overrideCursor() is None:
            QGuiApplication.setOverrideCursor(Qt.CursorShape.BlankCursor)


class ChromeHider:
    # Cada barra se oculta con la tecnica que su ciclo de vida en Anki tolera:
    #
    # - Menu (QMenuBar): colapso de altura con los metodos propios de Anki
    #   (hide_menubar/show_menubar). Ademas, mientras el menu esta oculto, sus
    #   acciones con atajo (Ctrl+Z deshacer, etc.) se re-anclan a la ventana
    #   principal: con la barra colapsada Qt deja de despachar los atajos que
    #   cuelgan del menu, y un atajo anclado a la ventana funciona siempre que
    #   la ventana este activa, se vea el menu o no. Al restaurar, se sueltan.
    # - Barra superior (TopWebView): setFixedHeight(0), NUNCA setVisible(False).
    #   Una webview Qt-oculta hace que las mediciones de altura devuelvan None y
    #   entonces Anki programa mw.reset() a 1000 ms, que expulsa del repaso.
    #   Colapsada pero visible, las mediciones siguen funcionando.
    # - Barra inferior (BottomWebView): se colapsa su CONTENIDO con CSS a altura
    #   cero, de modo que cada vez que Anki la mide (al entrar al repaso, al
    #   cambiar de tema, en su show() diferido) obtiene 0 y el la deja plegada.
    #   El hide() de Anki solo acelera el pliegue inicial.

    def __init__(self) -> None:
        self._menu_hidden: bool = False
        self._toolbar_hidden: bool = False
        self._bottom_hidden: bool = False
        self._menu_actions: list[QAction] = []

    @property
    def bottom_hidden(self) -> bool:
        return self._bottom_hidden

    def enter(self, config: HiderConfig) -> None:
        self._set_menu(hidden=config.hide_menu_bar)
        self._set_toolbar(hidden=config.hide_toolbar)
        self._set_bottom(hidden=config.hide_bottom_bar)

    def leave(self) -> None:
        self._set_menu(hidden=False)
        self._set_toolbar(hidden=False)
        # La barra inferior no se toca al salir: Anki ya llamo a su show() en la
        # limpieza del repaso y la pantalla siguiente redibuja y remide la barra
        # con contenido nuevo (sin nuestro CSS). Reexpandirla aqui mostraria los
        # botones del repaso durante la transicion.
        self._bottom_hidden = False

    def sync(self, config: HiderConfig) -> None:
        # Cambio de configuracion en pleno repaso: se ajusta solo lo que difiere.
        self._set_menu(hidden=config.hide_menu_bar)
        self._set_toolbar(hidden=config.hide_toolbar)
        self._set_bottom(hidden=config.hide_bottom_bar)

    def reassert(self) -> None:
        # Anki reexpande estas dos por su cuenta: la barra superior al remedir su
        # contenido tras un cambio de tema, y el menu via show_menubar() cuando la
        # ventana se maximiza o restaura. La inferior se recoloca sola (mide 0).
        if self._toolbar_hidden:
            toolbar = _widget(constants.TOOLBAR_ATTR)
            if toolbar is not None and toolbar.height() > 0:
                toolbar.setFixedHeight(0)
        if self._menu_hidden:
            bar = mw.menuBar()
            if bar is not None and bar.height() > 0:
                hide_fn = getattr(mw, "hide_menubar", None)
                if callable(hide_fn):
                    hide_fn()
                else:
                    bar.setFixedHeight(0)

    def _set_menu(self, *, hidden: bool) -> None:
        if hidden == self._menu_hidden:
            return
        if hidden:
            hide_fn = getattr(mw, "hide_menubar", None)
            if callable(hide_fn):
                hide_fn()
            else:
                bar = mw.menuBar()
                if bar is None:
                    return
                bar.setFixedHeight(0)
            self._grab_menu_shortcuts()
        else:
            self._release_menu_shortcuts()
            show_fn = getattr(mw, "show_menubar", None)
            if callable(show_fn):
                show_fn()
            else:
                bar = mw.menuBar()
                if bar is None:
                    return
                bar.setMinimumHeight(0)
                bar.setMaximumHeight(QWIDGETSIZE_MAX)
            bar = mw.menuBar()
            if bar is not None:
                bar.update()
        self._menu_hidden = hidden

    def _grab_menu_shortcuts(self) -> None:
        if self._menu_actions:
            return
        bar = mw.menuBar()
        if bar is None:
            return
        # Solo se anclan acciones con atajo que no estuvieran ya en la ventana,
        # y se apunta exactamente cuales, para soltar solo esas al restaurar.
        already: set[int] = {id(action) for action in mw.actions()}
        seen: set[int] = set()
        pending: list[QAction] = list(bar.actions())
        while pending:
            action = pending.pop()
            if id(action) in seen:
                continue
            seen.add(id(action))
            menu = action.menu()
            if menu is not None:
                pending.extend(menu.actions())
            if action.shortcut().isEmpty() or id(action) in already:
                continue
            mw.addAction(action)
            self._menu_actions.append(action)

    def _release_menu_shortcuts(self) -> None:
        for action in self._menu_actions:
            mw.removeAction(action)
        self._menu_actions.clear()

    def _set_toolbar(self, *, hidden: bool) -> None:
        if hidden == self._toolbar_hidden:
            return
        toolbar = _widget(constants.TOOLBAR_ATTR)
        if toolbar is None:
            return
        if hidden:
            toolbar.setFixedHeight(0)
        else:
            toolbar.setMinimumHeight(0)
            toolbar.setMaximumHeight(QWIDGETSIZE_MAX)
            # Se deja que Anki recalcule la altura correcta midiendo el contenido.
            adjust = getattr(toolbar, "adjustHeightToFit", None)
            if callable(adjust):
                adjust()
        self._toolbar_hidden = hidden

    def _set_bottom(self, *, hidden: bool) -> None:
        if hidden == self._bottom_hidden:
            return
        bottom = _widget(constants.BOTTOM_BAR_ATTR)
        if bottom is None:
            return
        if hidden:
            _eval_js(bottom, constants.HIDE_BOTTOM_BAR_JS)
            # hide() de BottomWebView: colapsa la altura del widget a 1 px con la
            # animacion propia de Anki (respeta "reducir movimiento").
            bottom.hide()
        else:
            _eval_js(bottom, constants.SHOW_BOTTOM_BAR_JS)
            # show() de BottomWebView remide el contenido (ya sin nuestro CSS) y
            # anima la barra hasta su altura real.
            bottom.show()
        self._bottom_hidden = hidden


class HiderManager:
    # Sin __slots__: PyQt necesita crear referencias debiles al conectar senales a
    # metodos de instancia, y es un singleton en el que slots no aporta nada.

    def __init__(self) -> None:
        self._config: HiderConfig = load_config()
        self._chrome = ChromeHider()
        self._cursor_hider = CursorHider(self._config.cursor_idle_ms, mw)
        self._active: bool = False
        self._skip_auto_start: bool = False
        self._theme_settle_timer = QTimer(mw)
        self._theme_settle_timer.setSingleShot(True)
        self._theme_settle_timer.setInterval(constants.THEME_SETTLE_MS)
        self._theme_settle_timer.timeout.connect(self._on_theme_settled)

    def reload_config(self) -> None:
        self._config = load_config()
        self._cursor_hider.set_idle_ms(self._config.cursor_idle_ms)
        if not self._active:
            return
        self._chrome.sync(self._config)
        if self._config.hide_cursor:
            self._cursor_hider.activate()
        else:
            self._cursor_hider.deactivate()

    def _report_error(self, hook_name: str, exc: Exception) -> None:
        _logger.exception("Hider: error en %s", hook_name, exc_info=exc)
        tooltip(tr("hook_error"), period=4000)

    def _enter_review(self) -> None:
        if self._active:
            return
        self._active = True
        self._skip_auto_start = False
        self._chrome.enter(self._config)
        if self._config.hide_cursor:
            self._cursor_hider.activate()

    def _leave_review(self) -> None:
        if not self._active:
            return
        self._active = False
        self._theme_settle_timer.stop()
        self._cursor_hider.deactivate()
        self._chrome.leave()

    def _on_theme_settled(self) -> None:
        try:
            if self._active:
                self._chrome.reassert()
        except Exception as exc:
            self._report_error("theme_settle", exc)

    def _allowed_eases(self, reviewer: Reviewer) -> frozenset[int]:
        return frozenset({constants.AGAIN_EASE, reviewer._defaultEase()})

    def on_state_will_change(self, new_state: str, old_state: str) -> None:
        # Se oculta ANTES de que Anki pinte el repaso: asi no hay ni un fotograma
        # con las barras puestas. Es seguro porque ya no se Qt-oculta ninguna
        # webview; la medicion de la barra inferior se encola hasta que carga el
        # contenido nuevo del repaso, que con nuestro CSS mide 0.
        try:
            if new_state == constants.REVIEW_STATE:
                self._enter_review()
            elif old_state == constants.REVIEW_STATE:
                self._leave_review()
                self._skip_auto_start = True
            if new_state == constants.DECK_BROWSER_STATE:
                self._skip_auto_start = False
        except Exception as exc:
            self._report_error("state_will_change", exc)

    def on_reviewer_did_show_question(self, card: Card) -> None:
        # Red de seguridad sincrona y barata: si algo reexpandio el menu o la barra
        # superior (cambio de tema, maximizar/restaurar la ventana), se recolapsan
        # como muy tarde en la siguiente tarjeta.
        try:
            if self._active:
                self._chrome.reassert()
        except Exception as exc:
            self._report_error("reviewer_did_show_question", exc)

    def on_theme_did_change(self) -> None:
        try:
            if self._active:
                self._theme_settle_timer.start()
        except Exception as exc:
            self._report_error("theme_did_change", exc)

    def on_overview_did_refresh(self, overview: Overview) -> None:
        try:
            if not self._config.auto_start_study or self._skip_auto_start:
                return
            if mw.col is None:
                return

            def _counts(col: Collection) -> tuple[int, int, int]:
                return col.sched.counts()

            def _start_if_due(counts: tuple[int, int, int]) -> None:
                if (
                    self._skip_auto_start
                    or mw.state != constants.OVERVIEW_STATE
                    or not any(counts)
                ):
                    return
                overview._linkHandler("study")

            QueryOp(parent=mw, op=_counts, success=_start_if_due).failure(
                lambda exc: self._report_error("overview_did_refresh", exc)
            ).run_in_background()
        except Exception as exc:
            self._report_error("overview_did_refresh", exc)

    def on_webview_will_set_content(self, web_content: WebContent, context: Any) -> None:
        try:
            if isinstance(context, Reviewer):
                if self._config.hide_scrollbar:
                    web_content.head += constants.HIDE_SCROLLBAR_CSS
            elif isinstance(context, ReviewerBottomBar):
                # El CSS viaja dentro del contenido de la barra: cualquier pagina
                # nueva de la barra inferior del repaso nace ya con altura cero y
                # todas las mediciones de Anki devuelven 0 por si solas.
                if self._config.hide_bottom_bar:
                    web_content.head += constants.HIDE_BOTTOM_BAR_CSS
        except Exception as exc:
            self._report_error("webview_will_set_content", exc)

    def on_reviewer_will_init_answer_buttons(
        self,
        buttons: tuple[tuple[int, str], ...],
        reviewer: Reviewer,
        card: Card,
    ) -> tuple[tuple[int, str], ...]:
        # Se filtra la lista (ease, etiqueta) que Anki usa para construir los botones,
        # en vez de ocultarlos por CSS: el numero de botones y el significado de cada
        # "ease" varian segun la tarjeta, asi que un selector fijo podria esconder "Bien".
        try:
            if not self._config.hide_hard_easy_buttons:
                return buttons
            allowed = self._allowed_eases(reviewer)
            filtered = tuple((ease, label) for ease, label in buttons if ease in allowed)
            return filtered or buttons
        except Exception as exc:
            self._report_error("reviewer_will_init_answer_buttons", exc)
            return buttons

    def on_reviewer_will_answer_card(
        self,
        ease_tuple: EaseTuple,
        reviewer: Reviewer,
        card: Card,
    ) -> EaseTuple:
        # Sin esto, los atajos 2 y 4 seguirian respondiendo con botones que no se ven.
        try:
            proceed, ease = ease_tuple
            if not proceed or not self._config.hide_hard_easy_buttons:
                return ease_tuple
            if ease in self._allowed_eases(reviewer):
                return ease_tuple
            tooltip(tr("button_hidden"), period=2000)
            return (False, ease)
        except Exception as exc:
            self._report_error("reviewer_will_answer_card", exc)
            return ease_tuple

    def on_profile_will_close(self) -> None:
        try:
            self._leave_review()
        except Exception as exc:
            self._report_error("profile_will_close", exc)


_active_manager: HiderManager | None = None


def set_active_manager(manager: HiderManager) -> None:
    global _active_manager
    _active_manager = manager


def reload_active_manager() -> None:
    if _active_manager is not None:
        _active_manager.reload_config()