from PyQt5 import QtWidgets, uic, QtCore
import sys
from functools import partial
import credential
import mysql.connector
import post

#sql for view post from user

class Viewpost(QtWidgets.QMainWindow):
    global mydb
    def __init__(self, parent = None):
       
        super(Viewpost, self).__init__()
        uic.loadUi('ui/viewpost.ui', self)
        self.currentIndex = 0
        #self.show()
        #self.usernameLabel.setText('')

    def update(self, user):
        postContent = post.getFollowerPosts(mydb, user, self.currentIndex)

    def login(self):
        username = self.usernameInput.text()
        password = self.passwordInput.text()
        if (credential.checkCredential(mydb, username, password)):
            print("success")
            #call the profile windows here
            self.profile.update(username)
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