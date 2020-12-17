from PyQt5 import QtWidgets, uic, QtCore
import sys
from functools import partial
from mydb import mydb
import post
import user

#write posts 
class CreatePostUI(QtWidgets.QDialog):
    global mydb
    def __init__(self,user, parent = None):
        super(CreatePostUI, self).__init__()
        uic.loadUi('WritePost.ui', self)
        self.POST_Button.clicked.connect(self.WritePost) 

    def updateUser(self, user):
        self.username = user
        
    def WritePost(self):
        username = self.username
        content = self.InputMessage.toPlainText()
        post.createPost(mydb, username, content)
        self.close()

# app = QtWidgets.QApplication(sys.argv)
# window = CreatePostUI()
# window.show()
# app.exec()   
