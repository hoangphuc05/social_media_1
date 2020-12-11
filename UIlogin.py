from PyQt5 import QtWidgets, uic
import sys
from functools import partial
import credential
import mysql.connector


class Ui(QtWidgets.QMainWindow):
    global mydb
    def __init__(self, parent = None):
       
        super(Ui, self).__init__()
        uic.loadUi('login.ui', self)
        self.show()
        self.newAccountButton.clicked.connect(self.newAccount)
        self.LoginButton.clicked.connect(self.login)
        self.registerAccount = Ui2(self)
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

class PopUp(QtWidgets.QDialog):
    def __init__(self, parent = None):
       
        super(PopUp, self).__init__()
        uic.loadUi('wrongPassword.ui', self)
        #self.show()
        self.buttonBox.accepted.connect(self.close)
        #self.usernameLabel.setText('')

    


class Ui2(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super(Ui2, self).__init__()
        uic.loadUi('listivew.ui', self)
        #self.show()
        

        #self.usernameLabel.setText('')


mydb = mysql.connector.connect(
    host="api.hphucs.me",
    user="cs300",
    password="Whitworth000",
    database="FinalProject"
)


app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec()