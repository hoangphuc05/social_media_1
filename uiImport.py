from PyQt5 import QtWidgets, uic
import sys

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('login.ui', self)
        self.show()

        #self.usernameLabel.setText('')

app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec()