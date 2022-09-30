from Classes import Player, Team, Game, Admin

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLabel, QLineEdit, QCheckBox


class Registration_Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, 1920, 1010)
        self.setWindowTitle('')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Registration_Window()
    ex.show()
    sys.exit(app.exec())
