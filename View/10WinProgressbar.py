from PySide2.QtWidgets import QApplication, QMainWindow, QProgressBar, QStatusBar, QLabel
import sys
from PySide2.QtGui import QIcon


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("ProgressBar")
        self.setGeometry(300, 200, 500, 400)

        self.statusLabel = QLabel("Showing Progress")
        self.progressbar = QProgressBar()
        self.progressbar.setMinimum(0)
        self.progressbar.setMaximum(100)

        self.setIcon()

        self.createStatusBar()

    def setIcon(self):
        appIcon = QIcon("icon/icon.png")
        self.setWindowIcon(appIcon)

    def createStatusBar(self):
        self.statusBar = QStatusBar()
        self.progressbar.setValue(20)
        self.statusBar.addWidget(self.statusLabel, 1)
        self.statusBar.addWidget(self.progressbar, 2)
        self.setStatusBar(self.statusBar)


myapp = QApplication(sys.argv)
window = Window()
window.show()

myapp.exec_()
sys.exit()