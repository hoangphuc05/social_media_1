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
        self.indexMax = 0
        self.nextButton.clicked.connect(self.nextPost)
        self.prevButton.clicked.connect(self.prevPost)
        #self.likeButton.clicked.connect(self.likePost)
        #self.saveButton.clicked.connect(self.savePost)
        #self.show()
        #self.usernameLabel.setText('')

    def update(self, user):
        self.currentUser = user
        postContent = post.getFollowerPosts(mydb, user, self.currentIndex)
        self.indexMax = post.countVisiblePost(mydb, user) - 1
        self.authorLabel.setText(str(postContent[1]))
        self.content.setText(str(postContent[2]))

    def nextPost(self):
        if self.currentIndex < self.indexMax:
            self.currentIndex += 1
        else:
            self.currentIndex = 0
        self.update(self.currentUser)
        print(self.currentIndex)

    def prevPost(self):
        if self.currentIndex > 0:
            self.currentIndex -= 1
        else:
            self.currentIndex = self.indexMax
        self.update(self.currentUser)
        print(self.currentIndex)

    def likePost(self):
        #like post here
        pass

    def savePost(self):
        #save post here
        pass
            




mydb = mysql.connector.connect(
    host="api.hphucs.me",
    user="cs300",
    password="Whitworth000",
    database="FinalProject"
)


app = QtWidgets.QApplication(sys.argv)
window = Viewpost()

window.show()
window.update("nhatminh")
app.exec()