# Copyright (C) 2026 AnkiCraft
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
from __future__ import annotations

from typing import Final

from aqt.qt import QEvent

PACKAGE_NAME: Final[str] = "hider"

# ── AnkiCraft branding ────────────────────────────────────────────────────────
ADDON_NAME: Final[str] = "Hider"
ADDON_DISPLAY_NAME: Final[str] = "Hider (by Ankicraft)"
ADDON_VERSION: Final[str] = "3.3.0"
AUTHOR_NAME: Final[str] = "AnkiCraft"
ANKIWEB_ID: Final[str] = "216116224"
ANKIWEB_PAGE_URL: Final[str] = f"https://ankiweb.net/shared/info/{ANKIWEB_ID}"
ANKIWEB_REVIEW_URL: Final[str] = f"https://ankiweb.net/shared/review/{ANKIWEB_ID}"
URL_KOFI: Final[str] = "https://ko-fi.com/ankicraft"
URL_PATREON: Final[str] = "https://www.patreon.com/cw/Ankicraft594"
URL_REPORT_BUG: Final[str] = ANKIWEB_PAGE_URL
LOGO_FILENAME: Final[str] = "logo.png"
LOGO_SIZE_PX: Final[int] = 72

# Palette
COLOR_ACCENT: Final[str] = "#7C5CE0"
COLOR_KOFI_BG: Final[str] = "#29ABE0"
COLOR_KOFI_HOVER: Final[str] = "#1E8FBF"
COLOR_PATREON_BG: Final[str] = "#FF424D"
COLOR_PATREON_HOVER: Final[str] = "#E0313C"
COLOR_RATE_BG: Final[str] = "#F5A623"
COLOR_RATE_HOVER: Final[str] = "#D98E12"

# Welcome dialog meta keys
CONFIG_KEY_META: Final[str] = "_meta"
META_KEY_WELCOME_SHOWN: Final[str] = "welcome_shown"
WELCOME_DELAY_MS: Final[int] = 2000

REVIEW_STATE: Final[str] = "review"
DECK_BROWSER_STATE: Final[str] = "deckBrowser"
OVERVIEW_STATE: Final[str] = "overview"

TOOLBAR_ATTR: Final[str] = "toolbarWeb"
BOTTOM_BAR_ATTR: Final[str] = "bottomWeb"

KEY_HIDE_MENU_BAR: Final[str] = "hide_menu_bar"
KEY_HIDE_TOOLBAR: Final[str] = "hide_toolbar"
KEY_HIDE_BOTTOM_BAR: Final[str] = "hide_bottom_bar"
KEY_HIDE_CURSOR: Final[str] = "hide_cursor"
KEY_CURSOR_IDLE_SECONDS: Final[str] = "cursor_idle_seconds"
KEY_HIDE_SCROLLBAR: Final[str] = "hide_scrollbar"
KEY_HIDE_HARD_EASY_BUTTONS: Final[str] = "hide_hard_easy_buttons"
KEY_AUTO_START_STUDY: Final[str] = "auto_start_study"

DEFAULT_CURSOR_IDLE_SECONDS: Final[int] = 3
MIN_CURSOR_IDLE_SECONDS: Final[int] = 1
MAX_CURSOR_IDLE_SECONDS: Final[int] = 60

AGAIN_EASE: Final[int] = 1

# Tras un cambio de tema, TopWebView vuelve a medir su altura de forma asincrona y
# reexpande la barra superior; se recolapsa pasado este margen.
THEME_SETTLE_MS: Final[int] = 300

MOUSE_EVENT_TYPES: Final[frozenset[QEvent.Type]] = frozenset(
    {QEvent.Type.MouseMove, QEvent.Type.HoverMove}
)

HIDE_SCROLLBAR_CSS: Final[str] = """
<style id="hider-hide-scrollbar">
    html { scrollbar-width: none; }
    ::-webkit-scrollbar { width: 0; height: 0; display: none; }
</style>
"""

BOTTOM_COLLAPSE_STYLE_ID: Final[str] = "hider-bottom-collapse"

# Colapsa el CONTENIDO de la barra inferior a altura cero. Anki decide la altura del
# widget midiendo document.documentElement.offsetHeight de esta pagina; con estas
# reglas toda medicion devuelve 0 y es el propio Anki quien mantiene la barra
# colapsada, sin que haga falta pelear con sus temporizadores ni animaciones.
# !important: deben ganar a las reglas de tamano de css/toolbar-bottom.css de Anki.
_BOTTOM_COLLAPSE_RULES: Final[str] = (
    "html{height:0 !important;min-height:0 !important;overflow:hidden !important}"
    "body{display:none !important}"
)

# Para paginas nuevas (se inyecta en el <head> via webview_will_set_content).
HIDE_BOTTOM_BAR_CSS: Final[str] = (
    f'<style id="{BOTTOM_COLLAPSE_STYLE_ID}">{_BOTTOM_COLLAPSE_RULES}</style>'
)

# Para la pagina ya cargada (se inyecta via eval). Idempotente: comprueba el id.
HIDE_BOTTOM_BAR_JS: Final[str] = f"""
(function(){{
    if (document.getElementById('{BOTTOM_COLLAPSE_STYLE_ID}')) return;
    var st = document.createElement('style');
    st.id = '{BOTTOM_COLLAPSE_STYLE_ID}';
    st.textContent = '{_BOTTOM_COLLAPSE_RULES}';
    document.head.appendChild(st);
}})();
"""

SHOW_BOTTOM_BAR_JS: Final[str] = f"""
(function(){{
    var st = document.getElementById('{BOTTOM_COLLAPSE_STYLE_ID}');
    if (st) st.remove();
}})();
"""