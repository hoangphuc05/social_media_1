from PyQt5 import QtWidgets, uic, QtCore
import sys
from functools import partial
import mysql.connector
import post
import user

#write posts 
class CreatePostUI(QtWidgets.QDialog):
    global mydb
    def __init__(self, parent = None):
        super(CreatePostUI, self).__init__()
        uic.loadUi('WritePost.ui', self)
        self.POST_Button.clicked.connect(self.WritePost)

    def WritePost(self):
        content = self.InputMessage.toPlainText()
        post.createPost(mydb, "pcai22", content)

  
mydb = mysql.connector.connect(
    host="api.hphucs.me",
    user="cs300",
    password="Whitworth000",
    database="FinalProject"
)

app = QtWidgets.QApplication(sys.argv)
window = CreatePostUI()
window.show()
app.exec()   
