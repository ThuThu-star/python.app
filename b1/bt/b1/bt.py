from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6 import uic
import sys

class Alert(QMessageBox):
    def error_message(self, title, message):
        self.setIcon(QMessageBox.Icon.Critical)
        self.setWindowTitle(title)
        self.setText(message)
        self.exec()
        
    def success_message(self, title, message):
        self.setIcon(QMessageBox.Icon.Information)
        self.setWindowTitle(title)
        self.setText(message)
        self.exec()

    class TemperatureCoverter(QWidget):
        def __init__(self):
            super().__init__()
            uic.loadUi("ui/login.ui", self)

            self.txt_Chieu_Cao = self.findchild(QLineEdit,"lineEdit")
            self.txt_Can_Nang = self.findchild(QLineEdit, "LineEdit_2")
            self.txt_Ket_Qua = self.findchild(QLineEdit, "LineEdit_4")
            self.txt_Phan_Loai = self.findchild(QLineEdit, "LineEdit_5")
            self.btn_Tinh_BMI = self.findchild(QPushButton, "pushButton")

            self.btn_Tinh_BMI.clicked.connect(self.chuyen_doi)
            self.btn_clear.clicked.connect(self.clear_all)

        def chuyen_doi(self):