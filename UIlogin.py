from PyQt5 import QtWidgets, uic, QtCore
import sys
from functools import partial
import credential
import mysql.connector
import UInewAccount
from UIpopup import PopUp


class Login(QtWidgets.QMainWindow):
    global mydb
    def __init__(self, parent = None):
       
        super(Login, self).__init__()
        uic.loadUi('login.ui', self)
        #self.show()
        self.newAccountButton.clicked.connect(self.newAccount)
        self.LoginButton.clicked.connect(self.login)
        self.registerAccount = UInewAccount.NewAcct(self)
        self.popup = PopUp(self)
        #self.usernameLabel.setText('')

    def newAccount(self):
        print("a")
        self.registerAccount.show()

    def login(self):
        username = self.usernameInput.text()
        password = self.passwordInput.text()
        if (credential.checkCredential(mydb, username, password)):
            print("success")
            #call the profile windows here
        else:
            print("Wrong password")
            self.popup.show()



mydb = mysql.connector.connect(
    host="api.hphucs.me",
    user="cs300",
    password="Whitworth000",
    database="FinalProject"
)


app = QtWidgets.QApplication(sys.argv)
window = Login()
window.show()
app.exec()