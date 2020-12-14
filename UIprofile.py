from PyQt5 import QtWidgets, uic, QtCore
import user
import follower
import sys
import mysql.connector
from UIpost import CreatePostUI
from UIviewpost import Viewpost

class Profile(QtWidgets.QMainWindow):
    global mydb
    def __init__(self, parent = None):
        
        super(Profile, self).__init__()
        uic.loadUi('profile.ui', self)
        self.createPost = CreatePostUI(self)
        self.createPostButton.clicked.connect(self.callWritePost)
        self.viewPostUI = Viewpost(self)
        self.viewpostButton.clicked.connect(self.viewAllPost)
        #get profile information

    def update(self, username):
        self.username = username
        profile = user.getAccount(mydb, username)[0]
        self.usernameLabel.setText(profile[0])
        #self.usernameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.firstNameLabel.setText(profile[1])
        self.lastNameLabel.setText(profile[2])
        self.genderValue.setText(profile[3])
        self.DoBValue.setText(str(profile[4]))
        self.followerCount.setText(str(follower.countFollowers(mydb, username)))
        self.show()

    def callWritePost(self):
        self.createPost.show() 

    def viewAllPost(self):
        self.viewPostUI.update(self.username)
        self.viewPostUI.show()





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