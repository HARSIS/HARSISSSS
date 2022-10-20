from Classes import Player, Team, Game, Admin

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLabel, QLineEdit, QCheckBox, QInputDialog
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt


class Registration_Window(QWidget):  # окно регистрации
    def __init__(self):
        super().__init__()
        self.nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']  # числа от 1 до 0
        self.initUI()
        self.cams = [False, False, False, False, False, False, False]  # камуфляжи

    def initUI(self):
        self.setGeometry(752, 400, 415, 430)
        self.setWindowTitle('Регистрация')

        self.welcome = QLabel(self)
        self.welcome.setText('<h1 style="color: rgb(0, 0, 0);">Приветствуем!</h1>')
        self.welcome.move(65, 20)
        self.welcome.setFont(QFont('Arial', 14))

        self.please = QLabel(self)
        self.please.setText("Зарегистрируйтесь чтобы продолжить")
        self.please.move(63, 65)
        self.please.setFont(QFont('Arial', 12))

        self.enter = QPushButton('войти', self)
        self.enter.resize(50, 22)
        self.enter.move(210, 380)
        self.enter.setFont(QFont('Arial', 12))
        self.enter.clicked.connect(self.open_enter_window)

        self.hate = QLabel(self)
        self.hate.setText("Уже заррегистрированы?")
        self.hate.setFont(QFont('Arial', 12))
        self.hate.move(22, 380)

        self.enter_number = QLabel(self)
        self.enter_number.setText("Номер телефона")
        self.enter_number.setFont(QFont('Arial', 14))
        self.enter_number.move(22, 125)

        self.input_number = QLineEdit(self)
        self.input_number.move(177, 125)
        self.input_number.resize(215, 24)
        self.input_number.setFont(QFont('Arial', 13))

        self.enter_pw = QLabel(self)
        self.enter_pw.setText("Пароль")
        self.enter_pw.setFont(QFont('Arial', 14))
        self.enter_pw.move(22, 150)

        self.input_pw = QLineEdit(self)
        self.input_pw.move(177, 150)
        self.input_pw.resize(215, 24)
        self.input_pw.setFont(QFont('Arial', 13))

        self.enter_name = QLabel(self)
        self.enter_name.setText("Фамилия, Имя")
        self.enter_name.setFont(QFont('Arial', 14))
        self.enter_name.move(22, 175)

        self.input_name = QLineEdit(self)
        self.input_name.move(177, 175)
        self.input_name.resize(215, 24)
        self.input_name.setFont(QFont('Arial', 13))

        self.enter_nick = QLabel(self)
        self.enter_nick.setText("Позывной")
        self.enter_nick.setFont(QFont('Arial', 14))
        self.enter_nick.move(22, 200)

        self.input_nick = QLineEdit(self)
        self.input_nick.move(177, 200)
        self.input_nick.resize(215, 24)
        self.input_nick.setFont(QFont('Arial', 13))

        self.enter_date = QLabel(self)
        self.enter_date.setText("Дата рождения")
        self.enter_date.setFont(QFont('Arial', 14))
        self.enter_date.move(22, 225)

        self.input_date = QLineEdit(self)
        self.input_date.move(177, 225)
        self.input_date.resize(215, 24)
        self.input_date.setFont(QFont('Arial', 13))

        self.enter_cam = QLabel(self)
        self.enter_cam.setText("Камуфляж")
        self.enter_cam.setFont(QFont('Arial', 14))
        self.enter_cam.move(22, 250)

        self.mc = QCheckBox('MC', self)
        self.mc.move(177, 250)
        self.mc.stateChanged.connect(self.MC)
        self.mc.setFont(QFont('Arial', 13))

        self.mox = QCheckBox('MOX', self)
        self.mox.move(225, 250)
        self.mox.stateChanged.connect(self.MOX)
        self.mox.setFont(QFont('Arial', 13))

        self.emr = QCheckBox('EMP', self)
        self.emr.move(283, 250)
        self.emr.stateChanged.connect(self.EMR)
        self.emr.setFont(QFont('Arial', 13))

        self.bk = QCheckBox('BK', self)
        self.bk.move(340, 250)
        self.bk.stateChanged.connect(self.BK)
        self.bk.setFont(QFont('Arial', 13))

        self.tan = QCheckBox('TAN', self)
        self.tan.move(177, 275)
        self.tan.stateChanged.connect(self.TAN)
        self.tan.setFont(QFont('Arial', 13))

        self.olive = QCheckBox('OLIVE', self)
        self.olive.move(232, 275)
        self.olive.stateChanged.connect(self.OLIVE)
        self.olive.setFont(QFont('Arial', 13))

        self.other = QCheckBox('ДРУГОЙ', self)
        self.other.move(303, 275)
        self.other.stateChanged.connect(self.OTHER)
        self.other.setFont(QFont('Arial', 13))

        self.enter_type = QLabel(self)
        self.enter_type.setText("Тип игрока")
        self.enter_type.setFont(QFont('Arial', 14))
        self.enter_type.move(22, 300)

        self.choose_type = QPushButton('Выбор', self)
        self.choose_type.resize(60, 24)
        self.choose_type.move(115, 300)
        self.choose_type.clicked.connect(self.open_choose_win)
        self.choose_type.setFont(QFont('Arial', 13))

        self.type2 = QLabel(self)
        self.type2.setText('                                    ')
        self.type2.setFont(QFont('Arial', 13))
        self.type2.move(177, 303)

        self.input = QPushButton('Зарегистрироваться', self)
        self.input.resize(190, 26)
        self.input.move(120, 340)
        self.input.clicked.connect(self.register)
        self.input.setFont(QFont('Arial', 14))

        self.error = QLabel(self)
        self.error.setText('<h1 style="color: rgb(150, 0, 0);">⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀</h1>')
        self.error.setFont(QFont('Arial', 7))
        self.error.move(22, 95)

    def open_enter_window(self):  # открываем окно для входа
        self.Enter_Window = Enter_Window()
        self.Enter_Window.show()
        self.close()

    # функции для добавления камуфляжей

    def MC(self, a):
        if a == Qt.Checked:
            self.cams[0] = True
        else:
            self.cams[0] = False

    def MOX(self, a):
        if a == Qt.Checked:
            self.cams[1] = True
        else:
            self.cams[1] = False

    def EMR(self, a):
        if a == Qt.Checked:
            self.cams[2] = True
        else:
            self.cams[2] = False

    def BK(self, a):
        if a == Qt.Checked:
            self.cams[3] = True
        else:
            self.cams[3] = False

    def TAN(self, a):
        if a == Qt.Checked:
            self.cams[4] = True
        else:
            self.cams[4] = False

    def OLIVE(self, a):
        if a == Qt.Checked:
            self.cams[5] = True
        else:
            self.cams[5] = False

    def OTHER(self, a):
        if a == Qt.Checked:
            self.cams[6] = True
        else:
            self.cams[6] = False

    def open_choose_win(self):  # окно выбора типа
        type, ok_pressed = QInputDialog.getItem(
            self, "", "Выберете тип игрока (основной)?",
            ("SQB (до 120м/c)", "Штурмовик (до 150м/с)", "Снайпер (до 170м/c)", "Щитовик"), 1, False)
        if ok_pressed:
            self.type2.setText(type)
            self.choose_type.setFont(QFont('Arial', 13))

    def register(self):  # пробуем зарегистрироваться, если данные корректны открываем основное приложение
        self.end_number = []
        self.number = list(self.input_number.text())
        for x in self.number:
            if x in self.nums:
                self.end_number.append(x)
        if self.end_number:
            if self.end_number[0] == '7':
                self.end_number[0] = '8'
            if len(self.end_number) != 11:
                self.error.setText('<h1 style="color: rgb(150, 0, 0);">Не корректный номер</h1>')
                return ''
            else:
                self.error.setText('<h1 style="color: rgb(150, 0, 0);"> </h1>')
        else:
            self.error.setText('<h1 style="color: rgb(150, 0, 0);">Введите номер телефона</h1>')
            return ''

        self.password = self.input_pw.text()
        if not (self.password):
            self.error.setText('<h1 style="color: rgb(150, 0, 0);">Ведите пароль</h1>')
            return ''
        else:
            self.error.setText('<h1 style="color: rgb(150, 0, 0);"> </h1>')

        self.name = self.input_name.text()
        if self.name:
            self.error.setText('<h1 style="color: rgb(150, 0, 0);"> </h1>')
        else:
            self.error.setText('<h1 style="color: rgb(150, 0, 0);">Не корректные фамилия и имя</h1>')
            return ''

        self.nick = self.input_nick.text()
        if self.nick:
            self.error.setText('<h1 style="color: rgb(150, 0, 0);"> </h1>')
        else:
            self.error.setText('<h1 style="color: rgb(150, 0, 0);">Не корректный позывной</h1>')
            return ''

        self.date = self.input_date.text()
        if self.date and '.' in self.date and len(self.date) == 10:
            if len(self.date.split('.')) == 3:
                self.error.setText('<h1 style="color: rgb(150, 0, 0);"> </h1>')
        elif not (self.date) or len(self.date) != 10 or not ('.' in self.date):
            self.error.setText('<h1 style="color: rgb(150, 0, 0);">Введите дату в формате 18.10.2022</h1>')
            return ''

        if True in self.cams:
            self.error.setText('<h1 style="color: rgb(150, 0, 0);"> </h1>')
        else:
            self.error.setText('<h1 style="color: rgb(150, 0, 0);">Выберете хотя бы один камуфляж</h1>')
            return ''

        if self.type2.text():
            self.error.setText('<h1 style="color: rgb(150, 0, 0);"> </h1>')
        else:
            self.error.setText('<h1 style="color: rgb(150, 0, 0);">Выберете основной тип</h1>')
            return ''

        print('done')


class Enter_Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(777, 400, 365, 112)
        self.setWindowTitle('Вход')

        self.go_back = QPushButton('Вернуться к регистрации', self)
        self.go_back.resize(255, 26)
        self.go_back.move(55, 72)
        self.go_back.clicked.connect(self.open_registration_window)
        self.go_back.setFont(QFont('Arial', 12))

        self.enter_number = QLabel(self)
        self.enter_number.setText("Номер телефона")
        self.enter_number.setFont(QFont('Arial', 14))
        self.enter_number.move(22, 20)

        self.input_number = QLineEdit(self)
        self.input_number.move(177, 20)
        self.input_number.resize(165, 24)
        self.input_number.setFont(QFont('Arial', 13))

        self.enter_pw = QLabel(self)
        self.enter_pw.setText("Пароль")
        self.enter_pw.setFont(QFont('Arial', 14))
        self.enter_pw.move(22, 44)

        self.input_pw = QLineEdit(self)
        self.input_pw.move(177, 44)
        self.input_pw.resize(165, 24)
        self.input_pw.setFont(QFont('Arial', 13))

    def open_registration_window(self):
        self.Registration_Window = Registration_Window()
        self.Registration_Window.show()
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Registration_Window()
    ex.show()
    sys.exit(app.exec())
