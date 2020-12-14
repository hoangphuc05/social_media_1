
from PyQt5 import QtWidgets, uic, QtCore
import sys
from functools import partial
import credential
import mysql.connector
from UIpopup import PopUp

class NewAcct(QtWidgets.QMainWindow):
    global mydb
    def __init__(self, parent = None, text= "Wrong username or password!"):
       
        super(NewAcct, self).__init__()
        uic.loadUi('newacct.ui', self)

        #add code to communicate with database and add account
        self.SignUpButton.clicked.connect(self.SignUp)
        self.popup = PopUp(self, "Password Does Not Match")
        self.newppop = PopUp(self,"New Account Created")

    def SignUp(self):
        Email = self.EmailInput.text()
        Password = self.PasswordInput.text()
        ConfirmPassword = self.ConfirmPasswordInput.text()
        FirstName = self.FirstNameInput.text()
        LastName = self.LastNameInput.text()
        Gender = self.GenderInput.text()

        temp_var = self.dateEdit.date() 
        dob = temp_var.toPyDate()

        if (Password != ConfirmPassword):
            self.popup.show()
        else:
            self.newppop.show()    


mydb = mysql.connector.connect(
    host="api.hphucs.me",
    user="cs300",
    password="Whitworth000",
    database="FinalProject"
)

app = QtWidgets.QApplication(sys.argv)
window = NewAcct()
window.show()
app.exec()