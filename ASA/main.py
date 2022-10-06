from Classes import Player, Team, Game, Admin

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLabel, QLineEdit, QCheckBox, QInputDialog
from PyQt5.QtGui import *


class Registration_Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.cams = ''

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
        self.enter.move(215, 94)
        self.enter.setFont(QFont('Arial', 12))
        self.enter.clicked.connect(self.open_enter_window)

        self.hate = QLabel(self)
        self.hate.setText("Уже заррегестрированы?")
        self.hate.setFont(QFont('Arial', 12))
        self.hate.move(22, 95)

        self.enter_number = QLabel(self)
        self.enter_number.setText("Номер телефона")
        self.enter_number.setFont(QFont('Arial', 14))
        self.enter_number.move(22, 125)

        self.input_number = QLineEdit(self)
        self.input_number.move(177, 125)
        self.input_number.resize(200, 24)
        self.input_number.setFont(QFont('Arial', 13))

        self.enter_pw = QLabel(self)
        self.enter_pw.setText("Пароль")
        self.enter_pw.setFont(QFont('Arial', 14))
        self.enter_pw.move(22, 150)

        self.input_pw = QLineEdit(self)
        self.input_pw.move(177, 150)
        self.input_pw.resize(200, 24)
        self.input_pw.setFont(QFont('Arial', 13))

        self.enter_name = QLabel(self)
        self.enter_name.setText("Фамилия, Имя")
        self.enter_name.setFont(QFont('Arial', 14))
        self.enter_name.move(22, 175)

        self.input_name = QLineEdit(self)
        self.input_name.move(177, 175)
        self.input_name.resize(200, 24)
        self.input_name.setFont(QFont('Arial', 13))

        self.enter_nick = QLabel(self)
        self.enter_nick.setText("Позывной")
        self.enter_nick.setFont(QFont('Arial', 14))
        self.enter_nick.move(22, 200)

        self.input_nick = QLineEdit(self)
        self.input_nick.move(177, 200)
        self.input_nick.resize(200, 24)
        self.input_nick.setFont(QFont('Arial', 13))

        self.enter_date = QLabel(self)
        self.enter_date.setText("Дата рождения")
        self.enter_date.setFont(QFont('Arial', 14))
        self.enter_date.move(22, 225)

        self.input_date = QLineEdit(self)
        self.input_date.move(177, 225)
        self.input_date.resize(200, 24)
        self.input_date.setFont(QFont('Arial', 13))

        self.enter_cam = QLabel(self)
        self.enter_cam.setText("Камуфляж")
        self.enter_cam.setFont(QFont('Arial', 14))
        self.enter_cam.move(22, 225)

        self.mc = QCheckBox('MC', self)
        self.mc.move(177, 225)
        self.mc.stateChanged.connect(self.app_mc)

        self.mox = QCheckBox('MOX', self)
        self.mox.move(177, 225)
        self.mox.stateChanged.connect(self.app_mc)

        self.mc = QCheckBox('MC', self)
        self.mc.move(177, 225)
        self.mc.stateChanged.connect(self.app_mc)

    def open_enter_window(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Registration_Window()
    ex.show()
    sys.exit(app.exec())
