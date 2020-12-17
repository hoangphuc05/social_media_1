from PyQt5 import QtWidgets, uic, QtCore
from PyQt5.QtGui import QImage, QPixmap
import user
import follower
import sys
import mysql.connector
from UIpost import CreatePostUI
from UIviewpost import Viewpost
import requests
from UIuserfinder import Follow


class Profile(QtWidgets.QMainWindow):
    global mydb
    def __init__(self, parent = None):
        
        super(Profile, self).__init__()
        uic.loadUi('profile.ui', self)
        self.createPost = CreatePostUI(self)
        self.createPostButton.clicked.connect(self.callWritePost)
        self.viewPostUI = Viewpost(self)
        
        self.viewpostButton.clicked.connect(self.viewAllPost)
        self.searchButton.clicked.connect(self.findUser)
        #get profile information

    def update(self, username):
        self.username = username
        profile = user.getAccount(mydb, username)[0]
        self.user = username

        self.searchUserUI = Follow(username, self)
        self.usernameLabel.setText(profile[0])
        #self.usernameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.firstNameLabel.setText(profile[1])
        self.lastNameLabel.setText(profile[2])
        self.genderValue.setText(profile[3])
        self.DoBValue.setText(str(profile[4]))
        self.followerCount.setText(str(follower.countFollowers(mydb, username)))

        #try to pull image from Whitworth
        whitworth = requests.get(f'https://www.whitworth.edu/administration/informationsystems/idcard/{self.user}.jpg')
        if whitworth.status_code == 200:
            ava  = QImage()
            ava.loadFromData(whitworth.content)
            self.ProfilePic.setPixmap(QPixmap(ava))
        self.show()



    def callWritePost(self):
        self.createPost.updateUser(self.user)
        self.createPost.show() 

    def viewAllPost(self):
        self.viewPostUI.update(self.username)
        self.viewPostUI.show()

    def findUser(self):
        self.searchUserUI.show()
        pass

    





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