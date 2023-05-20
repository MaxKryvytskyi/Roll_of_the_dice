import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import random

type_kub = 6
number_of_throws = 1

class Ui_main_window(object):
    def setupUi(self, main_window):
        main_window.setObjectName("main_window")
        main_window.resize(350, 500)
        main_window.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        main_window.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(main_window)
        self.centralwidget.setStyleSheet("background-color: rgb(187, 255, 200);")
        self.centralwidget.setObjectName("centralwidget")
        self.lcd_3 = QtWidgets.QLabel(self.centralwidget)
        self.lcd_3.setGeometry(QtCore.QRect(250, 100, 80, 30))
        self.lcd_3.setObjectName("lcd_3")
        self.select_cube = QtWidgets.QLabel(self.centralwidget)
        self.select_cube.setGeometry(QtCore.QRect(30, 10, 160, 35))
        self.select_cube.setObjectName("select_cube")
        self.number_of_cubes = QtWidgets.QLabel(self.centralwidget)
        self.number_of_cubes.setGeometry(QtCore.QRect(30, 220, 181, 41))
        self.number_of_cubes.setObjectName("number_of_cubes")
        self.throw_the_dice = QtWidgets.QPushButton(self.centralwidget)
        self.throw_the_dice.setGeometry(QtCore.QRect(130, 450, 90, 30))
        self.throw_the_dice.setObjectName("throw_the_dice")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(200, 180, 40, 30))
        self.label_5.setObjectName("label_5")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(200, 60, 40, 30))
        self.label_2.setObjectName("label_2")
        self.lcd_1 = QtWidgets.QLabel(self.centralwidget)
        self.lcd_1.setGeometry(QtCore.QRect(250, 20, 80, 30))
        self.lcd_1.setObjectName("lcd_1")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(200, 20, 40, 30))
        self.label_1.setObjectName("label_1")
        self.lcd_2 = QtWidgets.QLabel(self.centralwidget)
        self.lcd_2.setGeometry(QtCore.QRect(250, 60, 80, 30))
        self.lcd_2.setObjectName("lcd_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(200, 100, 40, 30))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(200, 140, 40, 30))
        self.label_4.setObjectName("label_4")
        self.lcd_4 = QtWidgets.QLabel(self.centralwidget)
        self.lcd_4.setGeometry(QtCore.QRect(250, 140, 80, 30))
        self.lcd_4.setObjectName("lcd_4")
        self.lcd_5 = QtWidgets.QLabel(self.centralwidget)
        self.lcd_5.setGeometry(QtCore.QRect(250, 180, 80, 30))
        self.lcd_5.setObjectName("lcd_5")
        self.lcd_9 = QtWidgets.QLabel(self.centralwidget)
        self.lcd_9.setGeometry(QtCore.QRect(250, 340, 80, 30))
        self.lcd_9.setObjectName("lcd_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(200, 380, 40, 30))
        self.label_10.setObjectName("label_10")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(200, 300, 40, 30))
        self.label_8.setObjectName("label_8")
        self.lcd_10 = QtWidgets.QLabel(self.centralwidget)
        self.lcd_10.setGeometry(QtCore.QRect(250, 380, 80, 30))
        self.lcd_10.setObjectName("lcd_10")
        self.lcd_8 = QtWidgets.QLabel(self.centralwidget)
        self.lcd_8.setGeometry(QtCore.QRect(250, 300, 80, 30))
        self.lcd_8.setObjectName("lcd_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(200, 340, 40, 30))
        self.label_9.setObjectName("label_9")
        self.lcd_6 = QtWidgets.QLabel(self.centralwidget)
        self.lcd_6.setGeometry(QtCore.QRect(250, 220, 80, 30))
        self.lcd_6.setObjectName("lcd_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(200, 260, 40, 30))
        self.label_7.setObjectName("label_7")
        self.lcd_7 = QtWidgets.QLabel(self.centralwidget)
        self.lcd_7.setGeometry(QtCore.QRect(250, 260, 80, 30))
        self.lcd_7.setObjectName("lcd_7")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(200, 220, 40, 30))
        self.label_6.setObjectName("label_6")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(30, 260, 137, 151))
        self.widget.setObjectName("widget")
        self.formLayout = QtWidgets.QFormLayout(self.widget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.but_kub_1 = QtWidgets.QRadioButton(self.widget)
        self.but_kub_1.setObjectName("but_kub_1")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.but_kub_1)
        self.but_kub_2 = QtWidgets.QRadioButton(self.widget)
        self.but_kub_2.setObjectName("but_kub_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.but_kub_2)
        self.but_kub_4 = QtWidgets.QRadioButton(self.widget)
        self.but_kub_4.setObjectName("but_kub_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.but_kub_4)
        self.but_kub_6 = QtWidgets.QRadioButton(self.widget)
        self.but_kub_6.setObjectName("but_kub_6")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.but_kub_6)
        self.but_kub_8 = QtWidgets.QRadioButton(self.widget)
        self.but_kub_8.setObjectName("but_kub_8")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.but_kub_8)
        self.but_kub_10 = QtWidgets.QRadioButton(self.widget)
        self.but_kub_10.setObjectName("but_kub_10")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.but_kub_10)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(30, 40, 131, 171))
        self.widget1.setObjectName("widget1")
        self.formLayout_2 = QtWidgets.QFormLayout(self.widget1)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.but_4 = QtWidgets.QRadioButton(self.widget1)
        self.but_4.setObjectName("but_4")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.but_4)
        self.but_6 = QtWidgets.QRadioButton(self.widget1)
        self.but_6.setObjectName("but_6")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.but_6)
        self.but_8 = QtWidgets.QRadioButton(self.widget1)
        self.but_8.setObjectName("but_8")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.but_8)
        self.but_12 = QtWidgets.QRadioButton(self.widget1)
        self.but_12.setObjectName("but_12")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.but_12)
        self.but_20 = QtWidgets.QRadioButton(self.widget1)
        self.but_20.setObjectName("but_20")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.but_20)
        self.but_100 = QtWidgets.QRadioButton(self.widget1)
        self.but_100.setObjectName("but_100")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.but_100)
        main_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

        self.add_function()
    
    def retranslateUi(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("main_window", "Roll of the dice"))
        self.select_cube.setText(_translate("main_window", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Оберіть куб</span></p></body></html>"))
        self.number_of_cubes.setText(_translate("main_window", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Кількість кубиків</span></p></body></html>"))
        self.throw_the_dice.setText(_translate("main_window", "Roll"))
        self.label_5.setText(_translate("main_window", "<html><head/><body><p align=\"right\"><span style=\" font-size:20pt; font-weight:600;\">5</span></p></body></html>"))
        self.label_2.setText(_translate("main_window", "<html><head/><body><p align=\"right\"><span style=\" font-size:20pt; font-weight:600;\">2</span></p></body></html>"))
        self.label_1.setText(_translate("main_window", "<html><head/><body><p align=\"right\"><span style=\" font-size:20pt; font-weight:600;\">1</span></p></body></html>"))
        self.label_3.setText(_translate("main_window", "<html><head/><body><p align=\"right\"><span style=\" font-size:20pt; font-weight:600;\">3</span></p></body></html>"))
        self.label_4.setText(_translate("main_window", "<html><head/><body><p align=\"right\"><span style=\" font-size:20pt; font-weight:600;\">4</span></p></body></html>"))
        self.label_10.setText(_translate("main_window", "<html><head/><body><p align=\"right\"><span style=\" font-size:20pt; font-weight:600;\">10</span></p></body></html>"))
        self.label_8.setText(_translate("main_window", "<html><head/><body><p align=\"right\"><span style=\" font-size:20pt; font-weight:600;\">8</span></p></body></html>"))
        self.label_9.setText(_translate("main_window", "<html><head/><body><p align=\"right\"><span style=\" font-size:20pt; font-weight:600;\">9</span></p></body></html>"))
        self.label_7.setText(_translate("main_window", "<html><head/><body><p align=\"right\"><span style=\" font-size:20pt; font-weight:600;\">7</span></p></body></html>"))
        self.label_6.setText(_translate("main_window", "<html><head/><body><p align=\"right\"><span style=\" font-size:20pt; font-weight:600;\">6</span></p></body></html>"))

        self.lcd_1.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; vertical-align:sub;\">100</span></p><p align=\"center\"><br/></p></body></html>"))
        self.lcd_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; vertical-align:sub;\">100</span></p><p align=\"center\"><br/></p></body></html>"))
        self.lcd_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; vertical-align:sub;\">100</span></p><p align=\"center\"><br/></p></body></html>"))
        self.lcd_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; vertical-align:sub;\">100</span></p><p align=\"center\"><br/></p></body></html>"))
        self.lcd_5.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; vertical-align:sub;\">100</span></p><p align=\"center\"><br/></p></body></html>"))
        self.lcd_6.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; vertical-align:sub;\">100</span></p><p align=\"center\"><br/></p></body></html>"))
        self.lcd_7.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; vertical-align:sub;\">100</span></p><p align=\"center\"><br/></p></body></html>"))
        self.lcd_8.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; vertical-align:sub;\">100</span></p><p align=\"center\"><br/></p></body></html>"))
        self.lcd_9.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; vertical-align:sub;\">100</span></p><p align=\"center\"><br/></p></body></html>"))
        self.lcd_10.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; vertical-align:sub;\">100</span></p><p align=\"center\"><br/></p></body></html>"))

        self.but_kub_1.setText(_translate("main_window", "1 - Гральні кісточки"))
        self.but_kub_2.setText(_translate("main_window", "2 -Гральні кісточки"))
        self.but_kub_4.setText(_translate("main_window", "4 - Гральні кісточки"))
        self.but_kub_6.setText(_translate("main_window", "6 - Гральні кісточки"))
        self.but_kub_8.setText(_translate("main_window", "8 - Гральні кісточки"))
        self.but_kub_10.setText(_translate("main_window", "10 - Гральні кісточки"))
        self.but_4.setToolTip(_translate("main_window", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">4 - Тетраэдр</span></p></body></html>"))
        self.but_4.setText(_translate("main_window", "4 - Тетраэдр"))
        self.but_6.setText(_translate("main_window", "6 - Куб"))
        self.but_8.setText(_translate("main_window", "8 - Октаэдр"))
        self.but_12.setText(_translate("main_window", "12 - Додекаэдр"))
        self.but_20.setText(_translate("main_window", "20 - Икосаэдр"))
        self.but_100.setText(_translate("main_window", "100 - Зоккиэдр"))


    def add_function(self):
        self.throw_the_dice.clicked.connect(self.result)
        self.but_100.clicked.connect(lambda: self.input_uzer("but_100"))
        self.but_20.clicked.connect(lambda: self.input_uzer("but_20"))
        self.but_12.clicked.connect(lambda: self.input_uzer("but_12"))
        self.but_8.clicked.connect(lambda: self.input_uzer("but_8"))
        self.but_6.clicked.connect(lambda: self.input_uzer("but_6"))
        self.but_4.clicked.connect(lambda: self.input_uzer("but_4"))

        self.but_kub_10.clicked.connect(lambda: self.input_uzer(10))
        self.but_kub_8.clicked.connect(lambda: self.input_uzer(8))
        self.but_kub_6.clicked.connect(lambda: self.input_uzer(6))
        self.but_kub_4.clicked.connect(lambda: self.input_uzer(4))
        self.but_kub_2.clicked.connect(lambda: self.input_uzer(2))
        self.but_kub_1.clicked.connect(lambda: self.input_uzer(1))

    def input_uzer(self, input_uzer):
        global type_kub 
        global number_of_throws 

        if input_uzer == "but_4":
            type_kub = 4
        elif input_uzer == "but_6":
            type_kub = 6
        elif input_uzer == "but_8":
            type_kub = 8
        elif input_uzer == "but_12":
            type_kub = 12
        elif input_uzer == "but_20":
            type_kub = 20
        elif input_uzer == "but_100":
            type_kub = 100
        
        if input_uzer == 1:
            number_of_throws = 1
        elif input_uzer == 2:
            number_of_throws = 2
        elif input_uzer == 4:
            number_of_throws = 4
        elif input_uzer == 6:
            number_of_throws = 6
        elif input_uzer == 8:
            number_of_throws = 8
        elif input_uzer == 10:
            number_of_throws = 10

    def result(self):
        self.lcd_1.setText("")
        self.lcd_2.setText("")
        self.lcd_3.setText("")
        self.lcd_4.setText("")
        self.lcd_5.setText("")
        self.lcd_6.setText("")
        self.lcd_7.setText("")
        self.lcd_8.setText("")
        self.lcd_9.setText("")
        self.lcd_10.setText("")
        if number_of_throws == 1:
            self.lcd_1.setText(str(random.randint(1, type_kub)))
        elif number_of_throws == 2:
            self.lcd_1.setText(str(random.randint(1, type_kub)))
            self.lcd_2.setText(str(random.randint(1, type_kub)))
        elif number_of_throws == 4:
            self.lcd_1.setText(str(random.randint(1, type_kub)))
            self.lcd_2.setText(str(random.randint(1, type_kub)))
            self.lcd_3.setText(str(random.randint(1, type_kub)))
            self.lcd_4.setText(str(random.randint(1, type_kub)))
        elif number_of_throws == 6:
            self.lcd_1.setText(str(random.randint(1, type_kub)))
            self.lcd_2.setText(str(random.randint(1, type_kub)))
            self.lcd_3.setText(str(random.randint(1, type_kub)))
            self.lcd_4.setText(str(random.randint(1, type_kub)))
            self.lcd_5.setText(str(random.randint(1, type_kub)))
            self.lcd_6.setText(str(random.randint(1, type_kub)))
        elif number_of_throws == 8:
            self.lcd_1.setText(str(random.randint(1, type_kub)))
            self.lcd_2.setText(str(random.randint(1, type_kub)))
            self.lcd_3.setText(str(random.randint(1, type_kub)))
            self.lcd_4.setText(str(random.randint(1, type_kub)))
            self.lcd_5.setText(str(random.randint(1, type_kub)))
            self.lcd_6.setText(str(random.randint(1, type_kub)))
            self.lcd_7.setText(str(random.randint(1, type_kub)))
            self.lcd_8.setText(str(random.randint(1, type_kub)))
        elif number_of_throws == 10:
            self.lcd_1.setText(str(random.randint(1, type_kub)))
            self.lcd_2.setText(str(random.randint(1, type_kub)))
            self.lcd_3.setText(str(random.randint(1, type_kub)))
            self.lcd_4.setText(str(random.randint(1, type_kub)))
            self.lcd_5.setText(str(random.randint(1, type_kub)))
            self.lcd_6.setText(str(random.randint(1, type_kub)))
            self.lcd_7.setText(str(random.randint(1, type_kub)))
            self.lcd_8.setText(str(random.randint(1, type_kub)))
            self.lcd_9.setText(str(random.randint(1, type_kub)))
            self.lcd_10.setText(str(random.randint(1, type_kub)))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui = Ui_main_window()
    ui.setupUi(main_window)
    main_window.show()
    sys.exit(app.exec_())
