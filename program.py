from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6 import uic

class Alert(QMessageBox):
    def error_message(self, title, message):
        self.selfcon(QMessageBox.Icon.Critical)
        self.setWindowTitle(title)
        self.setText(message)
        self.exec()

    def success_message(self, title, message):
        self.selfcon(QMessageBox.Icon.Information)
        self.setWindowTitle(title)
        self.setText(message)
        self.exec()

msg = Alert()

class Login(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/login.ui", self)
        
        self.email_input = self.findChild(QLineEdit, "txt_email")
        self.password_input = self.findChild(QLineEdit, "txt_password")
        self.btn_login = self.findChild(QPushButton, "btn_login")
        self.btn_register = self.findChild(QPushButton, "btn_register")
        self.btn_eye = self.findChild(QPushButton, "btn_eye")

        self.btn_eye.clicked.connect(lambda: self.show_password(self.btn_eye, self.password_input))
        self.btn_eye_login.clicked.connect(self.login)

    def show_password(self, button: QPushButton, input: QLineEdit):
        if input.echoMode() == QLineEdit.EchoMode.Password:
            input.setEchoMode(QLineEdit.EchoMode.Normal)
            button.selfIcon(QIcon("img/eye-solid.svq"))
        else:
            input.setEchoMode(QLineEdit.EchoMode.Password)
            button.setIcon(QIcon("img/eye-slash-solid.svg"))

    def login(self):
        email = self.email_input.text().strip()
        password = self.password_input.text().strip()

        if email == "":
            msg.error_message("Login", "Email is required")
            self.email_input.setFocus()
            return
        if password == "":
            msg.error_message("Login", "Password is required")
            self. password_input.setFocus()
            return
        
        with open("date/users.txt", "r") as file:
            for line in file:
                data = line.strip().split(",")
                if data[0] == email and data[1] == password:
                    msg.success_message("Login", "Welcome to the system")
                    return
                
        msg.error_message("Login", "Invalid email or password")
        self.email_input.setFocus()

    def show_register(self):
        self.register = Register()
        self.register.show()
#def__init__phuong thuc khoi tao