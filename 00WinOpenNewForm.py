from PySide2.QtWidgets import *
import sys
from PySide2.QtGui import QIcon, QFont




class Window(QWidget):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        self.setWindowTitle("Layout Managment")
        self.setGeometry(300, 200, 500, 400)

        self.setIcon()

        self.createLayout()
        vbox = QVBoxLayout()
        vbox.addWidget(self.groupBox)
        self.setLayout(vbox)

        self.show()

    def setIcon(self):
        appIcon = QIcon("icon.png")
        self.setWindowIcon(appIcon)

    def createLayout(self, parent=None):
        self.groupBox = QGroupBox("Please Choose One Language")
        self.groupBox.setFont(QFont("Sanserif", 13))

        hbox = QHBoxLayout()

        button = QPushButton("CSS", self)
        button.setIcon(QIcon("css.png"))
        button.setMinimumHeight(40)
        hbox.addWidget(button)
        # from View import Win
        # button.clicked.connect(Win.Start())
        button.clicked.connect(self.onClick)

        button1 = QPushButton("C++", self)
        button1.setIcon(QIcon("cpp.png"))
        button1.setMinimumHeight(40)
        hbox.addWidget(button1)

        button2 = QPushButton("Javascript", self)
        button2.setIcon(QIcon("javascript.png"))
        button2.setMinimumHeight(40)
        hbox.addWidget(button2)

        self.groupBox.setLayout(hbox)

    def onClick(self):
        from View import Win
        self.Sw = Win.Window()
        self.Sw.show()

#     def onClick(self):
#         self.SW = SecondWindow()
#         self.SW.show()
#         print("second")
#
# class SecondWindow(QWidget):
#     def __init__(self):
#         super(SecondWindow, self).__init__()
#         lbl = QLabel('Second Window', self)

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    MW = Window()
    MW.show()
    sys.exit(app.exec_())


# def Start():
#     myapp = QApplication(sys.argv)
#     window = Window()
#     window.show()
#
#     myapp.exec_()
#     sys.exit()
#
# Start()

