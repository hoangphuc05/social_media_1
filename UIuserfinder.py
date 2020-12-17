from PyQt5 import QtWidgets, uic
import sys
from functools import partial
import user
from UIprofile import Profile
from UIfollowprofile import FollowProfile
import mysql.connector
from UIpopup import PopUp


class Follow(QtWidgets.QMainWindow):
    global mydb
    def __init__(self, user,parent = None):

        super(Follow, self).__init__()
        uic.loadUi('userfinder.ui', self)
        self.cpopup = PopUp(self, "User Found")
        self.ipopup = PopUp(self,"User Not Found")
        self.profile = FollowProfile(user,self)

        self.seachbutton.clicked.connect(self.Search)
        
    def Search(self):
        Searchname = self.searchbox.text()

        val = user.getAccount(mydb,Searchname)

        if (len(val) == 0):
                self.ipopup.show()
        else:
            #self.cpopup.show()
            self.profile.update(Searchname)

            

                        

mydb = mysql.connector.connect(
    host="api.hphucs.me",
    user="cs300",
    password="Whitworth000",
    database="FinalProject"
)

if __name__ == '__main__':



    app = QtWidgets.QApplication(sys.argv)
    window = Follow("pcai22")
    window.show()
    app.exec()