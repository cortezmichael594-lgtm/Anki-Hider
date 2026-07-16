# Copyright (C) 2026 AnkiCraft
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
from __future__ import annotations

from aqt import mw
from aqt.qt import (
    QCheckBox,
    QDialog,
    QDialogButtonBox,
    QFrame,
    QGroupBox,
    QHBoxLayout,
    QSpinBox,
    QVBoxLayout,
    QWidget,
    qconnect,
)
from aqt.utils import showWarning, tooltip

from . import constants, logic
from .settings import DEFAULT_CONFIG, HiderConfig, load_config, save_config
from .strings import tr
from .support import build_support_row


def _checkbox(label_key: str, tip_key: str) -> QCheckBox:
    box = QCheckBox(tr(label_key))
    box.setToolTip(tr(tip_key))
    return box


class HiderOptionsDialog(QDialog):
    def __init__(self, parent: QWidget) -> None:
        super().__init__(parent)
        self.setWindowTitle(constants.ADDON_DISPLAY_NAME)
        self.setMinimumWidth(420)

        self._menu_bar = _checkbox("opt_menu_bar", "opt_menu_bar_tip")
        self._toolbar = _checkbox("opt_toolbar", "opt_toolbar_tip")
        self._bottom_bar = _checkbox("opt_bottom_bar", "opt_bottom_bar_tip")
        self._scrollbar = _checkbox("opt_scrollbar", "opt_scrollbar_tip")
        self._hard_easy = _checkbox("opt_hard_easy", "opt_hard_easy_tip")
        self._cursor = _checkbox("opt_cursor", "opt_cursor_tip")
        self._auto_start = _checkbox("opt_auto_start", "opt_auto_start_tip")

        self._idle_seconds = QSpinBox()
        self._idle_seconds.setRange(
            constants.MIN_CURSOR_IDLE_SECONDS, constants.MAX_CURSOR_IDLE_SECONDS
        )
        self._idle_seconds.setSuffix(tr("opt_cursor_suffix"))
        self._idle_seconds.setToolTip(tr("opt_cursor_tip"))
        qconnect(self._cursor.toggled, self._idle_seconds.setEnabled)

        cursor_row = QHBoxLayout()
        cursor_row.addWidget(self._cursor)
        cursor_row.addWidget(self._idle_seconds)
        cursor_row.addStretch()

        review_layout = QVBoxLayout()
        for widget in (self._menu_bar, self._toolbar, self._bottom_bar, self._scrollbar):
            review_layout.addWidget(widget)
        review_layout.addWidget(self._hard_easy)
        review_layout.addLayout(cursor_row)
        review_group = QGroupBox(tr("group_review"))
        review_group.setLayout(review_layout)

        behaviour_layout = QVBoxLayout()
        behaviour_layout.addWidget(self._auto_start)
        behaviour_group = QGroupBox(tr("group_behaviour"))
        behaviour_group.setLayout(behaviour_layout)

        buttons = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Save
            | QDialogButtonBox.StandardButton.Cancel
            | QDialogButtonBox.StandardButton.RestoreDefaults
        )
        qconnect(buttons.accepted, self.accept)
        qconnect(buttons.rejected, self.reject)
        self._relabel(buttons, QDialogButtonBox.StandardButton.Save, "btn_save")
        self._relabel(buttons, QDialogButtonBox.StandardButton.Cancel, "btn_cancel")
        restore = self._relabel(
            buttons, QDialogButtonBox.StandardButton.RestoreDefaults, "btn_defaults"
        )
        if restore is not None:
            qconnect(restore.clicked, lambda: self._apply(DEFAULT_CONFIG))

        separator = QFrame()
        separator.setFrameShape(QFrame.Shape.HLine)
        separator.setFrameShadow(QFrame.Shadow.Sunken)

        layout = QVBoxLayout()
        layout.addWidget(review_group)
        layout.addWidget(behaviour_group)
        layout.addWidget(buttons)
        layout.addWidget(separator)
        layout.addWidget(build_support_row(self))
        self.setLayout(layout)

        self._apply(load_config())
        self._menu_bar.setFocus()

    @staticmethod
    def _relabel(
        buttons: QDialogButtonBox,
        standard: QDialogButtonBox.StandardButton,
        key: str,
    ) -> QWidget | None:
        button = buttons.button(standard)
        if button is not None:
            button.setText(tr(key))
        return button

    def _apply(self, config: HiderConfig) -> None:
        self._menu_bar.setChecked(config.hide_menu_bar)
        self._toolbar.setChecked(config.hide_toolbar)
        self._bottom_bar.setChecked(config.hide_bottom_bar)
        self._scrollbar.setChecked(config.hide_scrollbar)
        self._hard_easy.setChecked(config.hide_hard_easy_buttons)
        self._cursor.setChecked(config.hide_cursor)
        self._idle_seconds.setValue(config.cursor_idle_seconds)
        self._idle_seconds.setEnabled(config.hide_cursor)
        self._auto_start.setChecked(config.auto_start_study)

    def selected_config(self) -> HiderConfig:
        return HiderConfig(
            hide_menu_bar=self._menu_bar.isChecked(),
            hide_toolbar=self._toolbar.isChecked(),
            hide_bottom_bar=self._bottom_bar.isChecked(),
            hide_cursor=self._cursor.isChecked(),
            cursor_idle_seconds=self._idle_seconds.value(),
            hide_scrollbar=self._scrollbar.isChecked(),
            hide_hard_easy_buttons=self._hard_easy.isChecked(),
            auto_start_study=self._auto_start.isChecked(),
        )


def open_options() -> None:
    dialog = HiderOptionsDialog(mw)
    if dialog.exec() != QDialog.DialogCode.Accepted:
        return
    try:
        save_config(dialog.selected_config())
    except Exception:
        showWarning(tr("save_failed"), parent=mw, title=tr("dialog_title"))
        return
    # writeConfig no dispara setConfigUpdatedAction, así que avisamos al manager
    # para que el cambio se note al momento, incluso en pleno repaso.
    logic.reload_active_manager()
    tooltip(tr("saved"), period=2000)
