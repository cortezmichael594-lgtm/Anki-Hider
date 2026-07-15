# Copyright (C) 2026 AnkiCraft
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
from __future__ import annotations

from aqt import gui_hooks, mw

from . import logic
from .logic import HiderManager
from .support import maybe_show_welcome
from .ui import open_options

__version__ = "3.3.0"


def _register(manager: HiderManager) -> None:
    gui_hooks.state_will_change.append(manager.on_state_will_change)
    gui_hooks.overview_did_refresh.append(manager.on_overview_did_refresh)
    gui_hooks.webview_will_set_content.append(manager.on_webview_will_set_content)
    gui_hooks.reviewer_did_show_question.append(manager.on_reviewer_did_show_question)
    gui_hooks.reviewer_will_init_answer_buttons.append(
        manager.on_reviewer_will_init_answer_buttons
    )
    gui_hooks.reviewer_will_answer_card.append(manager.on_reviewer_will_answer_card)
    gui_hooks.theme_did_change.append(manager.on_theme_did_change)
    gui_hooks.profile_will_close.append(manager.on_profile_will_close)

    logic.set_active_manager(manager)
    # setConfigAction hace que Anki abra este dialogo en lugar del editor de JSON.
    mw.addonManager.setConfigAction(__name__, open_options)

    gui_hooks.main_window_did_init.append(maybe_show_welcome)


_register(HiderManager())