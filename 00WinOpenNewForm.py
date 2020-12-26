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
        self.groupBox.setFont(QFont("Gotham Rounded Bold"))

        hbox = QHBoxLayout()

        button = QPushButton("CSS", self)
        button.setIcon(QIcon("css.png"))
        button.setMinimumHeight(40)
        check = QCheckBox('test')
        check.setToolTip('asdasdsd')

        spinbox = QSpinBox()
        spinbox.setPrefix("$")
        spinbox.setMaximum(100000000)

        self.currency = QLineEdit()
        self.currency.setInputMask('000 000 000 000 000')
        self.currency.textChanged.connect(self.currency_changed)

        # hbox.addWidget(spinbox)
        hbox.addWidget(self.currency)
        hbox.addWidget(button)
        hbox.addWidget(check)

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
        button2.clicked.connect(self.btn2)
        hbox.addWidget(button2)

        self.groupBox.setLayout(hbox)

    def currency_changed(self,value):
        pass
        # if len(value) == 4:
        #     self.currency.clearMask()
        #     self.currency.setInputMask('000,000'+'.00')
        #     self.currency.setCursorPosition(5)
        # elif len(value) == 7:
        #     self.currency.clearMask()
        #     self.currency.setInputMask('000,000,000')
        #     self.currency.setCursorPosition(8)
        # elif len(value) in [10,11,12]:
        #     self.currency.setInputMask('000,000,000,000')
        # elif len(value) in [13,14,15]:
        #     self.currency.setInputMask('000,000,000,000,000')
    def btn2(self):
        msg_box = QMessageBox()
        msg_box.setGeometry(50,50,10000,10000)
        msg_box.setWindowTitle('123')
        msg_box.setText('123')
        msg_box.setInformativeText('123')
        msg_box.setIcon(QMessageBox.Information)
        msg_box.exec_()
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

