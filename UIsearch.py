from PyQt5 import QtWidgets, uic
import sys
from functools import partial
import mysql.connector

class Ui3(QtWidgets.QMainWindow):
    global mydb
    def __init__(self, parent = None):
        super(Ui3, self).__init__()
        uic.loadUi('search.ui', self)
        self.show()
        self.pushButton.clicked.connect(self.search)

    def getFirstName(self, mydb, username):
        mycursor = mydb.cursor()
        sql = "SELECT Fname, Lname FROM USER WHERE UserName = %s"
        val = (username,)

        mycursor.execute(sql, val)

        myresult = mycursor.fetchall()

        return myresult

    def search(self):
        userName = self.textEdit.toPlainText()
        searchResult = self.getFirstName(mydb, userName)
        res = [''.join(i) for i in searchResult]
        self.listWidget.addItems(res)

mydb = mysql.connector.connect(
    host="api.hphucs.me",
    user="cs300",
    password="Whitworth000",
    database="FinalProject"
)

app = QtWidgets.QApplication(sys.argv)
windown = Ui3()
app.exec()