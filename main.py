import typing
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget

import sys

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        # Название окна, его отступ от єкрана и размер.
        self.setWindowTitle("Roll of the dice")
        self.setGeometry(500, 500, 500, 500)

        # Создание вивода текста по нажатию на кнопку.
        self.new_text = QtWidgets.QLabel(self)

        self.main_text = QtWidgets.QLabel(self)
        # делаем текс в програме
        self.main_text.setText("Кубики")
        self.main_text.move(200, 100)
        self.main_text.adjustSize()

        # создаем кликабельную кнопку.
        self.btn = QtWidgets.QPushButton(self)
        self.btn.move(200, 350)
        self.btn.setText("Нажми на меня")
        self.btn.setFixedWidth(200)
        self.btn.clicked.connect(self.Text)


    def Text(self):
        self.new_text.setText("Ти нажал на меня :D")
        self.new_text.move(100, 150)
        self.new_text.adjustSize()

def application():
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    application()