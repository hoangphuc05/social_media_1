
from PyQt5 import QtWidgets, uic, QtCore
import sys
from functools import partial
import credential
import mysql.connector

class NewAcct(QtWidgets.QMainWindow):
    global mydb
    def __init__(self, parent = None, text= "Wrong username or password!"):
       
        super(NewAcct, self).__init__()
        uic.loadUi('ui/newacct.ui', self)

        #add code to communicate with database and add account