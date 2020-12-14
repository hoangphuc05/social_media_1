

from PyQt5 import QtWidgets, uic, QtCore
import sys
from functools import partial
import credential
import mysql.connector
# def createPost(mydb, userID, postContent):
#     postID = post.createPost(mydb, userID, postContent)
#     action.createPost(mydb, userID, postID)

mydb = mysql.connector.connect(
    host="api.hphucs.me",
    user="cs300",
    password="Whitworth000",
    database="FinalProject"
)




class Test(QtWidgets.QMainWindow):
    def __init__(self, parent = None, text= "Wrong username or password!"):
       
        super(Test, self).__init__()
        uic.loadUi('listivew.ui', self)
        #self.show()
        # self.buttonBox.accepted.connect(self.close)
        # self.label.setText(text)
        # self.label.setAlignment(QtCore.Qt.AlignCenter)
        #self.usernameLabel.setText('')

app = QtWidgets.QApplication(sys.argv)
window = Test()
window.show()
app.exec()



