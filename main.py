from PyQt5 import QtWidgets, uic, QtCore
from PyQt5.QtGui import QImage, QPixmap

import UIlogin

app = QtWidgets.QApplication(sys.argv)
window = UIlogin.Login()
window.show()
app.exec()