from Classes import Player, Team, Game, Admin

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLabel, QLineEdit, QCheckBox, QFileDialog
from PyQt5.QtGui import *


class Registration_Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(500, 500, 600, 800)
        self.setWindowTitle('Регистрация')

        self.welcome = QLabel(self)
        self.welcome.setText('<h1 style="color: rgb(0, 0, 0);">Приветствуем!</h1>')
        self.welcome.move(20, 20)
        self.welcome.setFont(QFont('Arial', 14))

        self.please = QLabel(self)
        self.please.setText("Пожалуйста, зарегестрируйтесь чтобы продолжить")
        self.please.move(22, 65)
        self.please.setFont(QFont('Arial', 12))

        self.enter = QPushButton('войдите', self)
        self.enter.resize(70, 22)
        self.enter.move(215, 89)
        self.enter.setFont(QFont('Arial', 12))
        self.enter.clicked.connect(self.open_enter_window)

        self.hate = QLabel(self)
        self.hate.setText("Уже заррегестрированы?")
        self.hate.setFont(QFont('Arial', 12))
        self.hate.move(22, 90)

        self.enter_number = QLabel(self)
        self..setText("")
        self..move(, )

    def open_enter_window(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Registration_Window()
    ex.show()
    sys.exit(app.exec())
