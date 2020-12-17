from PyQt5 import QtWidgets, uic, QtCore
import sys
from functools import partial
import credential
from mydb import mydb
import post
import action
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
        self.likeButton.clicked.connect(self.likePost)
        #self.show()
        #self.usernameLabel.setText('')

    def update(self, user):
        self.currentUser = user
        postContent = post.getFollowerPosts(mydb, user, self.currentIndex)
        self.indexMax = post.countVisiblePost(mydb, user) - 1
        self.currentPostID = postContent[0]
        self.authorLabel.setText(str(postContent[1]))
        self.content.setText(str(postContent[2]))
        
        
        #number of likes
        likes = action.countLikes(mydb, self.currentPostID)
        self.likeCount.setText(str(likes) + " likes")
        
        #check if the user already like the post
        if action.checkLike(mydb, self.currentUser, self.currentPostID):
            self.likeButton.setText("Unlike")
            if not self.likeButton.isChecked():
                self.likeButton.toggle()
        else:
            self.likeButton.setText("Like")
            if self.likeButton.isChecked():
                self.likeButton.toggle()


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
        print(self.likeButton.text())
        if self.likeButton.text() == "Like":
            action.likePost(mydb, self.currentUser, self.currentPostID)
            self.likeButton.setText("Unlike")
            #self.likeButton.setCheckable(True)
        else:
            action.unlike(mydb, self.currentUser, self.currentPostID)
            self.likeButton.setText("Like")
            #self.likeButton.setCheckable(False)
        
        #number of likes
        likes = action.countLikes(mydb, self.currentPostID)
        self.likeCount.setText(str(likes) + " likes")

            




#app = QtWidgets.QApplication(sys.argv)
#window = Viewpost()

#window.show()
#window.update("pcai22")
#app.exec()