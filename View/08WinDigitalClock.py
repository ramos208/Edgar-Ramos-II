from PySide2.QtWidgets import QApplication, QWidget, QLCDNumber
from PySide2.QtCore import QTime, QTimer, SIGNAL
import sys
from PySide2.QtGui import QIcon, QFont


class Window(QLCDNumber):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        self.setSegmentStyle(QLCDNumber.Filled)

        timer = QTimer(self)
        self.connect(timer, SIGNAL('timeout()'), self.showTime,)


        timer.start(1000)

        self.showTime()
        self.setWindowTitle("Digital Clock")

        self.setIcon()

    def setIcon(self):
        appIcon = QIcon("icon/icon.png")
        self.setWindowIcon(appIcon)

    def showTime(self):
        time = QTime.currentTime()
        text = time.toString('hh:mm')
        if (time.second() % 2) == 0:
            text = text[:2] + ' ' + text[3:]

        self.display(text)





myApp = QApplication(sys.argv)
window = Window()
window.show()

# time.sleep(5)
window.resize(300,500)

myApp.exec_()
sys.exit(0)