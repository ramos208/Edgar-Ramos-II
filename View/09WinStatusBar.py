from PySide2.QtWidgets import QApplication, QWidget, QLCDNumber, QStatusBar, QMainWindow
from PySide2.QtCore import QTime, QTimer, SIGNAL
import sys
from PySide2.QtGui import QIcon, QFont


class Window(QMainWindow):
    def __init__(self):
        super().__init__()




        self.setWindowTitle("Status Bar")

        self.setIcon()
        self.createStatusBar()

    def setIcon(self):
        appIcon = QIcon("icon/icon.png")
        self.setWindowIcon(appIcon)

    def createStatusBar(self):
        self.myStatus = QStatusBar()
        self.myStatus.showMessage("Status Bar Is Ready", 3000)
        self.setStatusBar(self.myStatus)




myApp = QApplication(sys.argv)
window = Window()
window.show()

# time.sleep(5)
window.resize(300,500)

myApp.exec_()
sys.exit(0)