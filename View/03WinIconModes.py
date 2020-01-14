# from PySide2.QtWidgets import QApplication, QWidget , QLabel
from PySide2 import QtGui
from PySide2.QtWidgets import *
from PySide2.QtGui import *
import sys
import time


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Login")
        # self.setGeometry(300,300,300,400)

        self.setMinimumHeight(500)
        self.setMinimumWidth(750)
        self.setMaximumHeight(500)
        self.setMaximumWidth(750)

        self.setIcon()
        self.setlogo()

    def setIcon(self):
        appIcon = QIcon("icon/icon.png")
        self.setWindowIcon(appIcon)

    def setlogo(self):
        icon1 = QIcon("icon/icon.png")
        label1 = QLabel('Logo', self)
        pixmap1 = icon1.pixmap(120,120, QIcon.Active, QIcon.On)
        label1.setPixmap(pixmap1)
        label2 = QLabel('DRIVER', self)
        label2.move(40,120)
        # label2.setStyleSheet("QLabel {background-color: red;},font-weight: bold; font-size: 300")
        # label2.setStyleSheet("QLabel {color: red;},font-weight: bold; font-size: 200%")
        # bold = QtGui.QFont()
        # bold.setBold(True)
        # label2.setFont(bold)
        label2.setFont(QtGui.QFont("DRIVER",weight=QtGui.QFont.Bold))

        icon2 = QIcon("icon/icon.png")
        label3 = QLabel('Logo', self)
        pixmap2 = icon2.pixmap(120, 120, QIcon.Disabled, QIcon.Off)
        label3.setPixmap(pixmap2)
        label3.move(150, 0)

        label4 = QLabel('DRIVER', self)
        label4.move(190, 120)
        label4.setFont(QtGui.QFont("DRIVER", weight=QtGui.QFont.Bold))

        icon2 = QIcon("icon/icon.png")
        label5 = QLabel('Logo', self)
        pixmap2 = icon2.pixmap(120, 120, QIcon.Selected, QIcon.On)
        label5.setPixmap(pixmap2)
        label5.move(300, 0)


myApp = QApplication(sys.argv)
window = Window()
window.show()

# time.sleep(5)
window.resize(750,500)

myApp.exec_()
sys.exit(0)