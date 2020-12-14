from PyQt5 import QtWidgets, uic
import sys

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('listivew.ui', self)
        self.show()

        for i in range(50):
            itemN = QtWidgets.QListWidgetItem()
            itemN.setSizeHint(QtWidgets.QLabel("<h1>Hellow</h1>").sizeHint())
            self.listWidget.addItem(itemN)
            self.listWidget.setItemWidget(itemN, QtWidgets.QLabel("<h1>Hellow{0}</h1>".format(i)))
        
        #self.usernameLabel.setText('')

app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec()