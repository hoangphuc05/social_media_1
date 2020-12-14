from PyQt5 import QtWidgets, uic, QtCore
import user
import follower
import sys
import mysql.connector

class Profile(QtWidgets.QMainWindow):
    global mydb
    def __init__(self, parent = None):
        
        super(Profile, self).__init__()
        uic.loadUi('profile.ui', self)
        
        #get profile information

    def update(self, username):
        profile = user.getAccount(mydb, username)[0]
        self.usernameLabel.setText(profile[0])
        #self.usernameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.firstNameLabel.setText(profile[1])
        self.lastNameLabel.setText(profile[2])
        self.genderValue.setText(profile[3])
        self.DoBValue.setText(str(profile[4]))
        self.followerCount.setText(str(follower.countFollowers(mydb, username)))
        self.show()




mydb = mysql.connector.connect(
    host="api.hphucs.me",
    user="cs300",
    password="Whitworth000",
    database="FinalProject"
)


# app = QtWidgets.QApplication(sys.argv)
# window = Profile('pcai22')
# window.show()
# app.exec()