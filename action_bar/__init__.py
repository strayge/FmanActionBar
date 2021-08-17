import traceback
from PyQt5.QtCore import QEvent, QObject, pyqtSignal
from PyQt5.QtWidgets import QHBoxLayout, QPushButton, QVBoxLayout, QWidget
from fbs_runtime.application_context import cached_property
from fman import DirectoryPaneListener, _get_app_ctxt, load_json, run_application_command, show_alert


class NewMainWidget(QWidget):
    def __init__(self, parent, splitter):
        super().__init__(parent)
        self.parent = parent
        self.splitter = splitter
        self._set_layout()
        self.panes = []
        self.pane = None
        event_filter.focusIn.connect(self.focus_event)

    def new_pane_created(self, pane):
        """Store all DirectoryPane instances."""
        self.panes.append(pane)
        pane._widget._file_view.installEventFilter(event_filter)
        if not self.pane:
            self.pane = pane

    def focus_event(self, widget):
        """Detect last active pane."""
        for pane in self.panes:
            if pane._widget._file_view == widget:
                self.pane = pane
                return

    def _set_layout(self):
        self.main_layout = QVBoxLayout()
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

        self.top_bar = QHBoxLayout()
        self.bottom_bar = QHBoxLayout()

        for widget in self.get_top_widgets():
            self.top_bar.addWidget(widget)

        for widget in self.get_bottom_widgets():
            self.bottom_bar.addWidget(widget)

        self.main_layout.addLayout(self.top_bar)
        self.main_layout.addWidget(self.splitter)
        self.main_layout.addLayout(self.bottom_bar)

        self.setLayout(self.main_layout)

    def get_top_widgets(self):
        for setting in self.settings.get('top', []):
            widget = self.setting_to_widget(setting)
            if widget:
                yield widget

    def get_bottom_widgets(self):
        for setting in self.settings.get('bottom', []):
            widget = self.setting_to_widget(setting)
            if widget:
                yield widget

    def setting_to_widget(self, setting):
        text = setting[0]
        button = QPushButton(text)
        action_name = setting[1] if len(setting) >= 2 else None
        action_params = setting[2] if len(setting) >= 3 else None
        if action_name.startswith('app:'):
            button.clicked.connect(lambda: self.run_app_command(action_name[4:], action_params))
        else:
            button.clicked.connect(lambda: self.run_pane_command(action_name, action_params))
        return button

    def run_pane_command(self, command, params):
        try:
            self.pane.run_command(command, args=params)
        except Exception as e:
            show_alert(traceback.format_exc())

    def run_app_command(self, command, params):
        try:
            run_application_command(command, args=params)
        except Exception as e:
            show_alert(traceback.format_exc())

    @cached_property
    def settings(self):
        return load_json('action_bar.json')


class InputFocusFilter(QObject):
    focusIn = pyqtSignal(object)
    def eventFilter(self, widget, event):
        if event.type() == QEvent.FocusIn:
            # emit a `focusIn` signal, with the widget as its argument
            self.focusIn.emit(widget)
        return super().eventFilter(widget, event)


class PaneInitDetection(DirectoryPaneListener):
    def __init__(self, *a, **kw):
        super().__init__(*a, **kw)
        main_widget.new_pane_created(self.pane)


event_filter = InputFocusFilter()
window = _get_app_ctxt().main_window
main_widget = NewMainWidget(window, window._splitter)
window.setCentralWidget(main_widget)
