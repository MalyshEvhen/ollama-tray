import subprocess
import sys

from PySide2.QtGui import QIcon
from PySide2.QtWidgets import (QAction, QApplication, QMenu, QMessageBox,
                               QSystemTrayIcon, QWidget)


def run_ollama_list():
    try:
        # Run the 'ollama list' command and capture its output
        output = subprocess.check_output(["ollama", "list"], stderr=subprocess.STDOUT, universal_newlines=True)
        # Show the output in a pop-up message box
        QMessageBox.information(None, "Ollama List Output", output)
    except subprocess.CalledProcessError as e:
        # If the command fails, show the error message in a pop-up
        QMessageBox.warning(None, "Error", f"Failed to run 'ollama list': {e.output}")


class TrayApp:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.tray_icon = QSystemTrayIcon()
        self.tray_icon.setIcon(QIcon("assets/ollama.png"))  # Path to your icon image
        self.tray_icon.setVisible(True)
        self.tray_icon.setContextMenu(self.build_menu())

    def build_menu(self):
        menu = QMenu(title="Ollama", parent=None)

        # Add a button to the menu
        cmd_action = QAction("Run ollama list", self.app)
        cmd_action.triggered.connect(run_ollama_list)
        menu.addAction(cmd_action)

        # Add a Quit button
        quit_action = QAction("Quit", self.app)
        quit_action.triggered.connect(self.app.quit)
        menu.addAction(quit_action)

        return menu


if __name__ == "__main__":
    app = TrayApp()
    sys.exit(app.app.exec_())
