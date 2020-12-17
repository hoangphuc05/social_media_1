from PyQt5 import QtWidgets, uic, QtCore
import sys
from functools import partial
import mysql.connector 
import post
import user

# User interface defined for Posts 
class CreatePostUI(QtWidgets.QDialog):
    global mydb
    def __init__(self,user, parent = None):
        super(CreatePostUI, self).__init__()
        uic.loadUi('WritePost.ui', self)
        self.POST_Button.clicked.connect(self.WritePost) # sends a signal to execute the action

    def updateUser(self, user):
        self.username = user
        
    # call the createPost() defined in the Post class. 
    def WritePost(self):
        username = self.username # user that creates the post
        content = self.InputMessage.toPlainText() # capture message from the GUI
        post.createPost(mydb, username, content)
        self.close()
  
mydb = mysql.connector.connect(
    host="api.hphucs.me",
    user="cs300",
    password="Whitworth000",
    database="FinalProject"
)

