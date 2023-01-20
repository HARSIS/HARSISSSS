import sys


from screeninfo import get_monitors
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLabel, QLineEdit, QCheckBox, QInputDialog
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt


for monitor in get_monitors():
    if monitor.is_primary:
        size_x = monitor.width
        size_y = monitor.height
kx = size_x / 1920
ky = size_y / 1080
km = min(kx, ky)

def set_size(name, size_x, size_y, pos_x, pos_y):
    name.resize(round(size_x * kx), round(size_y * ky))
    name.move(round(pos_x * kx), round(pos_y * ky))
    name.setFont(QFont('Arial', round(25 * km)))
    return name

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(round(660 * kx), round(40 * ky), round(600 * kx), round(800 * ky))
        self.setWindowTitle('Simple Exampe')

        self.button1 = QPushButton('0', self)
        self.button1 = set_size(self.button1, 400, 200, 100, 300)
        self.button1.clicked.connect(self.plus)

    def plus(self):
        self.button1.setText(str(int(self.button1.text()) + 1))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())


