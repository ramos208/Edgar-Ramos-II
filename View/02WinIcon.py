from PySide2.QtWidgets import QApplication, QWidget
import sys
from PySide2.QtGui import QIcon

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Login")
        # self.setGeometry(300,300,300,400)

        # self.setGeometry(300,300,300,400)

        self.setMinimumHeight(500)
        self.setMinimumWidth(300)
        self.setMaximumHeight(500)
        self.setMaximumWidth(300)

        self.setIcon()

    def setIcon(self):
        appIcon = QIcon("icon/icon.png")
        self.setWindowIcon(appIcon)

myApp = QApplication(sys.argv)
window = Window()
window.show()

# time.sleep(5)
window.resize(300,500)

myApp.exec_()
sys.exit(0)