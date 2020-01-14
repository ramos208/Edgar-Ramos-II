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

        QToolTip.setFont(QFont("Decorative",10, QFont.Bold))
        self.setToolTip("Driver Login")

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
        label1.setToolTip("Active On")
        label2 = QLabel('Active', self)
        label2.move(40,120)
        label2.setFont(QtGui.QFont("DRIVER",weight=QtGui.QFont.Bold))

        icon2 = QIcon("icon/icon.png")
        label3 = QLabel('Logo', self)
        pixmap2 = icon2.pixmap(120, 120, QIcon.Disabled, QIcon.Off)
        label3.setPixmap(pixmap2)
        label3.move(150, 0)
        label3.setToolTip("Disabled Off")

        label4 = QLabel('Disabled', self)
        label4.move(185, 120)
        label4.setFont(QtGui.QFont("DRIVER", weight=QtGui.QFont.Bold))

        icon2 = QIcon("icon/icon.png")
        label5 = QLabel('Logo', self)
        pixmap2 = icon2.pixmap(120, 120, QIcon.Selected, QIcon.On)
        label5.setPixmap(pixmap2)
        label5.move(300, 0)
        label5.setToolTip("Disabled Off")
        label4 = QLabel('Selected', self)
        label4.move(335, 120)
        label4.setFont(QtGui.QFont("DRIVER", weight=QtGui.QFont.Bold))


myApp = QApplication(sys.argv)
window = Window()
window.show()

# time.sleep(5)
window.resize(750,500)

myApp.exec_()
sys.exit(0)