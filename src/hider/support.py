# Copyright (C) 2026 AnkiCraft
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
from __future__ import annotations

import os

from aqt import mw
from aqt.qt import (
    QDesktopServices,
    QDialog,
    QFrame,
    QHBoxLayout,
    QLabel,
    QPixmap,
    QPushButton,
    QSizePolicy,
    QTimer,
    QUrl,
    QVBoxLayout,
    QWidget,
    Qt,
    qconnect,
)

from . import constants
from .settings import is_welcome_shown, mark_welcome_shown
from .strings import tr


def _colored_button(label: str, bg: str, hover: str, tooltip: str = "") -> QPushButton:
    btn = QPushButton(label)
    if tooltip:
        btn.setToolTip(tooltip)
    btn.setStyleSheet(
        f"""
        QPushButton {{
            background-color: {bg};
            color: white;
            border: none;
            border-radius: 6px;
            padding: 6px 14px;
            font-weight: bold;
        }}
        QPushButton:hover {{
            background-color: {hover};
        }}
        """
    )
    return btn


def _open_url(url: str) -> None:
    QDesktopServices.openUrl(QUrl(url))


class WelcomeDialog(QDialog):
    def __init__(self, parent: QWidget) -> None:
        super().__init__(parent)
        self.setWindowTitle(
            tr("welcome_title", name=constants.ADDON_NAME, version=constants.ADDON_VERSION)
        )
        self.setMinimumWidth(480)

        layout = QVBoxLayout()
        layout.setSpacing(10)

        # ── Logo ──────────────────────────────────────────────────────────────
        logo_path = os.path.join(
            os.path.dirname(__file__), constants.LOGO_FILENAME
        )
        if os.path.isfile(logo_path):
            logo_label = QLabel()
            pixmap = QPixmap(logo_path).scaled(
                constants.LOGO_SIZE_PX,
                constants.LOGO_SIZE_PX,
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation,
            )
            logo_label.setPixmap(pixmap)
            logo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            layout.addWidget(logo_label)

        # ── Title ─────────────────────────────────────────────────────────────
        title_label = QLabel(
            tr("welcome_title", name=constants.ADDON_NAME, version=constants.ADDON_VERSION)
        )
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setStyleSheet(
            f"font-size: 16px; font-weight: bold; color: {constants.COLOR_ACCENT};"
        )
        layout.addWidget(title_label)

        # ── By line ───────────────────────────────────────────────────────────
        by_label = QLabel(f"by {constants.AUTHOR_NAME}")
        by_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        by_label.setStyleSheet("color: gray; font-size: 11px;")
        layout.addWidget(by_label)

        # ── Body ──────────────────────────────────────────────────────────────
        body_label = QLabel(
            tr("welcome_body", name=constants.ADDON_NAME)
        )
        body_label.setWordWrap(True)
        body_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(body_label)

        # ── Support note ──────────────────────────────────────────────────────
        note_label = QLabel(tr("welcome_support_note"))
        note_label.setWordWrap(True)
        note_label.setStyleSheet("color: gray; font-size: 11px;")
        layout.addWidget(note_label)

        # ── Buttons ───────────────────────────────────────────────────────────
        btn_row = QHBoxLayout()
        btn_row.setSpacing(8)

        kofi_btn = _colored_button(
            tr("kofi_button"),
            constants.COLOR_KOFI_BG,
            constants.COLOR_KOFI_HOVER,
            tr("kofi_tooltip"),
        )
        qconnect(kofi_btn.clicked, lambda: _open_url(constants.URL_KOFI))

        patreon_btn = _colored_button(
            tr("patreon_button"),
            constants.COLOR_PATREON_BG,
            constants.COLOR_PATREON_HOVER,
        )
        qconnect(patreon_btn.clicked, lambda: _open_url(constants.URL_PATREON))

        rate_btn = _colored_button(
            tr("rate_button"),
            constants.COLOR_RATE_BG,
            constants.COLOR_RATE_HOVER,
        )
        # Only show rate/review button when ANKIWEB_ID is set
        if constants.ANKIWEB_ID:
            qconnect(rate_btn.clicked, lambda: _open_url(constants.ANKIWEB_REVIEW_URL))
        else:
            rate_btn.setVisible(False)

        close_btn = QPushButton(tr("welcome_close"))
        close_btn.setDefault(True)
        close_btn.setAutoDefault(True)
        qconnect(close_btn.clicked, self.accept)

        btn_row.addWidget(kofi_btn)
        btn_row.addWidget(patreon_btn)
        if constants.ANKIWEB_ID:
            btn_row.addWidget(rate_btn)
        btn_row.addStretch()
        btn_row.addWidget(close_btn)

        layout.addLayout(btn_row)
        self.setLayout(layout)
        close_btn.setFocus()


def maybe_show_welcome() -> None:
    if is_welcome_shown():
        return
    # Marcar ANTES de mostrarse para que un crash no provoque un bucle.
    mark_welcome_shown()
    QTimer.singleShot(
        constants.WELCOME_DELAY_MS,
        lambda: WelcomeDialog(mw).exec(),
    )


def build_support_row(parent: QWidget) -> QWidget:
    """Pie sobrio para el diálogo de configuración (sin colores de marca)."""
    container = QWidget(parent)
    row = QHBoxLayout(container)
    row.setContentsMargins(0, 0, 0, 0)

    version_str = tr("version_line", name=constants.ADDON_NAME, version=constants.ADDON_VERSION)
    if constants.ANKIWEB_ID:
        left_html = (
            f'{version_str} · <a href="{constants.URL_REPORT_BUG}">'
            f'{tr("report_button")}</a>'
        )
    else:
        left_html = version_str

    left_label = QLabel(left_html)
    left_label.setOpenExternalLinks(True)
    left_label.setStyleSheet("font-size: 11px; color: gray;")
    row.addWidget(left_label)
    row.addStretch()

    kofi_btn = QPushButton(tr("kofi_button"))
    kofi_btn.setToolTip(tr("kofi_tooltip"))
    qconnect(kofi_btn.clicked, lambda: _open_url(constants.URL_KOFI))
    row.addWidget(kofi_btn)

    patreon_btn = QPushButton(tr("patreon_button"))
    qconnect(patreon_btn.clicked, lambda: _open_url(constants.URL_PATREON))
    row.addWidget(patreon_btn)

    if constants.ANKIWEB_ID:
        rate_btn = QPushButton(tr("rate_button"))
        qconnect(rate_btn.clicked, lambda: _open_url(constants.ANKIWEB_REVIEW_URL))
        row.addWidget(rate_btn)

    return container
