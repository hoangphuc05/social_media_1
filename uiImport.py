from PyQt5 import QtWidgets, uic
import sys
from functools import partial

class Ui(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super(Ui, self).__init__()
        uic.loadUi('login.ui', self)
        self.show()
        self.newAccount.clicked.connect(self.getLoginInfo)
        self.registerAccount = Ui2(self)
        #self.usernameLabel.setText('')

    def newAccount(self):
        print("a")
        self.registerAccount.show()

class Ui2(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super(Ui2, self).__init__()
        uic.loadUi('listivew.ui', self)
        #self.show()
        

        #self.usernameLabel.setText('')



app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec()