# This Python file uses the following encoding: utf-8
import sys
import os
import random

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader


class PasswordGenerator(QMainWindow):
    def __init__(self):
        super(PasswordGenerator, self).__init__()
        loader = QUiLoader()
        self.ui = loader.load('form.ui')
        self.ui.show()
        self.lenght=0
        self.l_chars='abcdefghijklmnopqrstuvwxyz'
        self.u_chars='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.numbers='0123456789'
        self.special='=+-*/!@#$%^|.'
        self.pas=[]
        self.ui.rbtn_standard.clicked.connect(self.setMode)
        self.ui.rbtn_strong.clicked.connect(self.setMode)
        self.ui.rbtn_super.clicked.connect(self.setMode)

    def setMode(self):

        if self.ui.rbtn_standard.isChecked():
            self.standard_pass()

        elif self.ui.rbtn_strong.isChecked():
            self.strong_pass()

        elif self.ui.rbtn_super.isChecked():
            self.super_pass()

    def standard_pass(self):
        self.pas=[]
        for i in range(5):
            self.pas.append(self.l_chars[random.randint(0,25)])
        self.pas.append(self.u_chars[random.randint(0,25)])
        self.pas.append(self.numbers[random.randint(0,9)])
        self.pas.append(self.special[random.randint(0,12)])
        self.show()

    def strong_pass(self):
        self.lenght=12
        self.pas=[]
        t=random.randint(1,4)
        for i in range(t):
            self.pas.append(self.u_chars[random.randint(0, 25)])
        self.lenght -=t
        t = random.randint(1, 4)
        for i in range(t):
            self.pas.append(self.numbers[random.randint(0, 9)])
        self.lenght -= t
        t = random.randint(1, 4)
        for i in range(t):
            self.pas.append(self.special[random.randint(0, 12)])
        self.lenght -= t
        for i in range(self.lenght):
            self.pas.append(self.l_chars[random.randint(0,25)])
        self.show()

    def super_pass(self):
        self.lenght = 20
        self.pas = []
        t = random.randint(1, 5)
        for i in range(t):
            self.pas.append(self.u_chars[random.randint(0, 25)])
        self.lenght -= t
        t = random.randint(1, 5)
        for i in range(t):
            self.pas.append(self.numbers[random.randint(0, 9)])
        self.lenght -= t
        t = random.randint(1, 5)
        for i in range(t):
            self.pas.append(self.special[random.randint(0, 12)])
        self.lenght -= t
        for i in range(self.lenght):
            self.pas.append(self.l_chars[random.randint(0, 25)])
        self.show()

    def show(self):
        temp=''
        random.shuffle(self.pas)
        for i in self.pas:
            temp+=str(i)
        self.ui.lbl_pass.setText(temp)


if __name__ == "__main__":
    app = QApplication([])
    widget = PasswordGenerator()
    sys.exit(app.exec())
