from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
import sys
from shifr import *
Form, Window = uic.loadUiType("main.ui")
app = QApplication([])
window1 = Window()
form1 = Form()
form1.setupUi(window1)
window1.show()
Form2, Window2 = uic.loadUiType("регистрация.ui")
window2 = Window2()
form2 = Form2()
form2.setupUi(window2)
Form3, Window3 = uic.loadUiType("личный кабинет.ui")
window3 = Window3()
form3 = Form3()
form3.setupUi(window3)
Form4, Window4 = uic.loadUiType("выход.ui")
window4 = Window4()
form4 = Form4()
form4.setupUi(window4)

form1.plainTextEdit.setReadOnly(True)
form4.lineEdit.setReadOnly(True)
form3.lineEdit.setReadOnly(True)


def login():
    def lk():
        form1.plainTextEdit.setPlainText("Главная")
        window3.show()
        window1.close()

        def enc():
            file2 = open("зашифровка.txt", "w+", encoding='UTF-8')
            file2.write(encrypt(form3.lineEdit_2.displayText().lower()))
            file2.close()
        def dec():
            file3 = open("расшифровка.txt", "w+", encoding='UTF-8')
            file3.write(decrypt(form3.lineEdit_2.displayText()))
            file3.close()

        def ext():
            window4.show()
            print("exit")
            def nope():
                window4.close()
            def yep():
                window4.close()
                window3.close()
                window1.show()
            form4.pushButton.clicked.connect(yep)
            form4.pushButton_2.clicked.connect(nope)

        form3.pushButton.clicked.connect(enc)
        form3.pushButton_2.clicked.connect(dec)
        form3.pushButton_3.clicked.connect(ext)
    def auth():
        window2.close()
        window1.show()
        d = open("data.txt", "r+", encoding='UTF-8')
        if f"логин: {encrypt(form1.lineEdit.displayText())}\nпароль: {encrypt(form1.lineEdit_2.displayText())}\n" in d.read() and form1.lineEdit_2.displayText():
            lk()
        else:
            form1.plainTextEdit.setPlainText("Неверный логин или пароль")
        d.close()
    def reg():
        window2.show()
        window1.close()
        def du():
            if form2.lineEdit_2.displayText() != " " and form2.lineEdit_3.displayText() != " ":
                data_read = open("data.txt", "r+", encoding='UTF-8')
                if f"логин: {encrypt(form2.lineEdit_2.displayText())}\n" in data_read.read():
                    form2.lineEdit.setText("Пользователь уже существует")
                elif form2.lineEdit_2.displayText() != "" and form2.lineEdit_3.displayText() != "":
                    data_add = open("data.txt", "a+", encoding='UTF-8')
                    data_add.write(f"\nлогин: {encrypt(form2.lineEdit_2.displayText())}\nпароль: {encrypt(form2.lineEdit_3.displayText())}\n")
                    data_add.close()
                    data_read.close()
                    window2.close()
                    lk()
                data_read.close()
        form1.plainTextEdit.setPlainText("Главная")
        form2.pushButton_2.clicked.connect(du)
        form2.pushButton.clicked.connect(auth)
    form1.pushButton_2.clicked.connect(reg)
    form1.pushButton.clicked.connect(auth)


login()
sys.exit(app.exec_())

