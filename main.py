from Classes import Player, Team, Game, Admin

import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLabel, QLineEdit, QCheckBox, QInputDialog
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt


class Registration_Window(QWidget):  # Создаем окно регистрации
    def __init__(self):
        super().__init__()
        self.nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9',
                     '0']  # Элементы, которые останутся в номере после преобразований
        self.initUI()
        self.cams = [False, False, False, False, False, False, False]  # Камуфляжи выбраннные игроком
        self.type_chosen = False

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

        self.enter = QPushButton('войти', self)  # Кнопка для перехода к окну входа
        self.enter.resize(50, 22)
        self.enter.move(212, 380)
        self.enter.setFont(QFont('Arial', 12))
        self.enter.clicked.connect(self.open_enter_window)

        self.hate = QLabel(self)
        self.hate.setText("Уже заррегистрированы?")
        self.hate.setFont(QFont('Arial', 12))
        self.hate.move(22, 380)

        self.enter_number = QLabel(self)  # Поля для ввода данных
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
        self.enter_name.setText("Фамилия и Имя")
        self.enter_name.setFont(QFont('Arial', 14))
        self.enter_name.move(22, 175)

        self.input_name = QLineEdit(self)
        self.input_name.move(177, 175)
        self.input_name.resize(215, 24)
        self.input_name.setFont(QFont('Arial', 13))

        self.enter_nick = QLabel(self)
        self.enter_nick.setText("Позывной")
        self.enter_nick.setFont(QFont('Arial', 14))
        self.enter_nick.move(22, 225)

        self.input_nick = QLineEdit(self)
        self.input_nick.move(177, 225)
        self.input_nick.resize(215, 24)
        self.input_nick.setFont(QFont('Arial', 13))

        self.enter_date = QLabel(self)
        self.enter_date.setText("Дата рождения")
        self.enter_date.setFont(QFont('Arial', 14))
        self.enter_date.move(22, 200)

        self.input_date = QLineEdit(self)
        self.input_date.move(177, 200)
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
        self.type2.setText('                                                                        ')
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

    def open_enter_window(self):  # Открываем окно для входа
        self.Enter_Window = Enter_Window()
        self.Enter_Window.show()
        self.close()

    # Функции для добавления камуфляжей

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

    def open_choose_win(self):  # Окно выбора типа
        type, ok_pressed = QInputDialog.getItem(
            self, "", "Выберете тип игрока (основной)?",
            ("SQB⠀(до⠀120м/c)", "Штурмовик⠀(до⠀150м/с)", "Снайпер⠀(до⠀170м/c)", "Щитовик"), 1, False)
        if ok_pressed:
            self.type2.setText(type)
            self.choose_type.setFont(QFont('Arial', 13))
            self.type_chosen = True

    def register(self):  # Пробуем зарегистрироваться, если данные корректны открываем основное приложение
        self.end_number = []
        self.number = list(self.input_number.text())
        for x in self.number:
            if x in self.nums:
                self.end_number.append(x)
        self.phone_number = ''
        if self.end_number:
            if self.end_number[0] == '7':
                self.end_number[0] = '8'

            for x in self.end_number:
                self.phone_number += x
            if len(self.end_number) != 11:
                self.error.setText('<h1 style="color: rgb(150, 0, 0);">Не корректный номер</h1>')
                return ''
            else:
                self.error.setText('<h1 style="color: rgb(150, 0, 0);"> </h1>')
        else:
            self.error.setText('<h1 style="color: rgb(150, 0, 0);">Введите номер телефона</h1>')
            return ''
        self.con = sqlite3.connect("ASA.sqlite")
        self.cur = self.con.cursor()
        self.available_phones = self.cur.execute("""SELECT phone FROM Players
                WHERE phone = ?""", (int(self.phone_number),)).fetchall()
        self.cursed_number = '[(' + self.phone_number + ',)]'
        self.con.commit()
        self.con.close()

        if self.cursed_number == str(self.available_phones):
            self.error.setText('<h1 style="color: rgb(150, 0, 0);">Номер телефона занят</h1>')
            return ''
        else:
            self.error.setText('<h1 style="color: rgb(150, 0, 0);"> </h1>')

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
            self.error.setText('<h1 style="color: rgb(150, 0, 0);">Введите фамилию и имя</h1>')
            return ''

        self.date = self.input_date.text()
        if self.date and '.' in self.date and len(self.date) == 10:
            if len(self.date.split('.')) == 3:
                self.error.setText('<h1 style="color: rgb(150, 0, 0);"> </h1>')
        elif not (self.date) or len(self.date) != 10 or not ('.' in self.date):
            self.error.setText('<h1 style="color: rgb(150, 0, 0);">Введите дату в формате 18.10.2022</h1>')
            return ''

        self.nick = self.input_nick.text()
        if self.nick:
            self.error.setText('<h1 style="color: rgb(150, 0, 0);"> </h1>')
        else:
            self.error.setText('<h1 style="color: rgb(150, 0, 0);">Не корректный позывной</h1>')
            return ''

        if True in self.cams:
            self.error.setText('<h1 style="color: rgb(150, 0, 0);"> </h1>')
        else:
            self.error.setText('<h1 style="color: rgb(150, 0, 0);">Выберете хотя бы один камуфляж</h1>')
            return ''

        if self.type_chosen is True:
            self.error.setText('<h1 style="color: rgb(150, 0, 0);"> </h1>')
        else:
            self.error.setText('<h1 style="color: rgb(150, 0, 0);">Выберете основной тип</h1>')
            return ''

        self.cams_cout = 0
        self.end_cams = ''
        for x in self.cams:
            self.cams_cout += 1
            if x is True:
                if self.cams_cout == 1:
                    self.end_cams = self.end_cams + 'MC, '
                elif self.cams_cout == 2:
                    self.end_cams = self.end_cams + 'MOX, '
                elif self.cams_cout == 3:
                    self.end_cams = self.end_cams + 'EMR, '
                elif self.cams_cout == 4:
                    self.end_cams = self.end_cams + 'BK, '
                elif self.cams_cout == 5:
                    self.end_cams = self.end_cams + 'TAN, '
                elif self.cams_cout == 6:
                    self.end_cams = self.end_cams + 'OLIVE, '
                elif self.cams_cout == 7:
                    self.end_cams = self.end_cams + 'Другой, '
        self.end_cams = self.end_cams[:-2]
        print(self.phone_number, self.password, self.name, self.date, self.nick, self.end_cams, self.type2.text())
        self.con = sqlite3.connect("ASA.sqlite")
        self.cur = self.con.cursor()
        self.cur.execute("""INSERT INTO Players VALUES (?, ?, ?, ?, ?, ?, ?)""", (
        self.phone_number, self.password, self.name, self.date, self.nick, self.end_cams, self.type2.text()))
        self.con.commit()
        self.con.close()


class Enter_Window(QWidget):  # Создаем окно для входа
    def __init__(self):
        super().__init__()
        self.initUI()
        self.nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9',
                     '0']  # Элементы, которые останутся в номере после преобразований

    def initUI(self):
        self.setGeometry(777, 400, 365, 140)
        self.setWindowTitle('Вход')

        self.go_back = QPushButton('Вернуться к регистрации', self)  # Кнопка для возврата на экран регистрации
        self.go_back.resize(220, 26)
        self.go_back.move(22, 72)
        self.go_back.clicked.connect(self.open_registration_window)
        self.go_back.setFont(QFont('Arial', 12))

        self.enter_number = QLabel(self)  # Поля для ввода данных
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

        self.enter = QPushButton('Войти', self)  # Кнопка для входа
        self.enter.resize(100, 26)
        self.enter.move(242, 72)
        self.enter.clicked.connect(self.open_main_window)
        self.enter.setFont(QFont('Arial', 12))

        self.error = QLabel(self)
        self.error.setText('<h1 style="color: rgb(150, 0, 0);">⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀</h1>')
        self.error.setFont(QFont('Arial', 7))
        self.error.move(22, 98)

    def open_main_window(self):
        self.end_number = []
        self.number = list(self.input_number.text())
        for x in self.number:
            if x in self.nums:
                self.end_number.append(x)
        self.phone_number = ''
        if self.end_number:
            if self.end_number[0] == '7':
                self.end_number[0] = '8'

            for x in self.end_number:
                self.phone_number += x
            if len(self.end_number) != 11:
                self.error.setText('<h1 style="color: rgb(150, 0, 0);">Не корректный номер</h1>')
                return ''
            else:
                self.error.setText('<h1 style="color: rgb(150, 0, 0);"> </h1>')
        else:
            self.error.setText('<h1 style="color: rgb(150, 0, 0);">Введите номер телефона</h1>')
            return ''
        self.con = sqlite3.connect("ASA.sqlite")
        self.cur = self.con.cursor()
        self.available_phones = self.cur.execute("""SELECT phone FROM Players
                        WHERE phone = ?""", (self.phone_number,)).fetchall()
        self.a = self.cur.execute("""SELECT phone FROM PLAYERS""")
        self.cursed_number = "[('" + self.phone_number + "',)]"
        self.con.commit()
        self.con.close()
        if self.cursed_number == str(self.available_phones):
            self.error.setText('<h1 style="color: rgb(150, 0, 0);"> </h1>')
        else:
            self.error.setText('<h1 style="color: rgb(150, 0, 0);">Не зарегистрированный номер</h1>')
            return ''
        self.password = self.input_pw.text()
        self.con = sqlite3.connect("ASA.sqlite")
        self.cur = self.con.cursor()
        self.available_passsword = self.cur.execute("""SELECT password FROM Players
                                WHERE phone = ?""", (int(self.phone_number),)).fetchall()
        self.cursed_password = "[('" + self.password + "',)]"
        self.con.commit()
        self.con.close()
        if str(self.available_passsword) == self.cursed_password:
            self.error.setText('<h1 style="color: rgb(150, 0, 0);"> </h1>')
            print('done')
        else:
            self.error.setText('<h1 style="color: rgb(150, 0, 0);">Неверный пароль</h1>')
            return ''

    def open_registration_window(self):  # Функция возвращения на экран регистрации
        self.Registration_Window = Registration_Window()
        self.Registration_Window.show()
        self.close()


if __name__ == '__main__':  # Запуск и выключение программы
    app = QApplication(sys.argv)
    ex = Registration_Window()
    ex.show()
    sys.exit(app.exec())
