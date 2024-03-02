import sys

from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QApplication, QAction, QSystemTrayIcon, QMenu


class TrayApp:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.tray_icon = QSystemTrayIcon()
        self.tray_icon.setIcon(QIcon("assets/ollama.png"))
        self.tray_icon.setVisible(True)
        self.tray_icon.setContextMenu(self.build_menu())

    def build_menu(self):
        menu = QMenu()
        quit_action = QAction("Quit", self.app)
        quit_action.triggered.connect(self.app.quit)
        menu.addAction(quit_action)
        return menu


if __name__ == "__main__":
    app = TrayApp()
    sys.exit(app.app.exec_())
