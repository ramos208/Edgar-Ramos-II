from PySide2.QtWidgets import *
from PySide2.QtGui import *
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PushButton")
        # self.setGeometry(300,300,300,400)

        # self.setGeometry(300,300,300,400)

        self.setMinimumHeight(500)
        self.setMinimumWidth(300)
        self.setMaximumHeight(500)
        self.setMaximumWidth(300)

        self.setIcon()
        self.setButton()
        self.center()

    def setIcon(self):
        appIcon = QIcon("icon/icon.png")
        self.setWindowIcon(appIcon)

    def setButton(self):
        btnLogin = QPushButton("Login", self)
        btnLogin.move(50,200)

        btnQuit = QPushButton("Quit", self)
        btnQuit.move(170, 200)

        btnQuit.clicked.connect(self.quitApp)

    def quitApp(self):
        userInfo = QMessageBox.question(self, "Confirmation", "Do You Want To Quit The Application",
                                        QMessageBox.Yes | QMessageBox.No)
        if userInfo == QMessageBox.Yes:
            myApp.quit()
        elif userInfo == QMessageBox.No:
            pass

    def center(self):
        qRect = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qRect.moveCenter(centerPoint)
        self.move(qRect.topLeft())




myApp = QApplication(sys.argv)
window = Window()
window.show()

# time.sleep(5)
window.resize(300,500)

myApp.exec_()
sys.exit(0)