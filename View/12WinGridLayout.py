from sched import scheduler

from PySide2.QtCore import Qt
from PySide2.QtWidgets import *
import sys
from PySide2.QtGui import QIcon, QFont


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Grid Layout")
        self.setGeometry(300, 200, 500, 400)

        self.setIcon()

        self.createGridLayout()
        vbox = QVBoxLayout()
        vbox.addWidget(self.groupBox)
        self.setLayout(vbox)

        self.show()

    def setIcon(self):
        appIcon = QIcon("icon.png")
        self.setWindowIcon(appIcon)

    def createGridLayout(self):
        self.groupBox = QGroupBox("Please Choose One Language")
        self.groupBox.setFont(QFont("Sanserif", 13))
        gridLayout = QGridLayout()

        edit = QLineEdit()
        gridLayout.addWidget(edit, 0, 0)

        button = QPushButton("C++", self)
        button.setIcon(QIcon("cpp.png"))
        gridLayout.addWidget(button, 0, 0)

        button1 = QPushButton("CSS", self)
        button1.setIcon(QIcon("css.png"))
        gridLayout.addWidget(button1, 0, 1)

        button11 = QPushButton("CSS", self)
        button11.setIcon(QIcon("css.png"))
        gridLayout.addWidget(button11, 0, 2)

        button2 = QPushButton("javascript", self)
        button2.setIcon(QIcon("javascript.png"))
        gridLayout.addWidget(button2, 1, 0)

        button3 = QPushButton("C#", self)
        button3.setIcon(QIcon("csharp.png"))
        gridLayout.addWidget(button3, 1, 1)

        button4 = QPushButton("Python", self)
        button4.setIcon(QIcon("pythonicon.png"))
        gridLayout.addWidget(button4, 2, 0)

        button5 = QPushButton("Java", self)
        button5.setIcon(QIcon("java.png"))
        gridLayout.addWidget(button5, 2, 1)

        button5.clicked.connect(self.btn5)

        self.groupBox.setLayout(gridLayout)

    def btn5(self):
        dialog = QDialog()

        scroll = QScrollArea()
        group = QGroupBox(scroll)
        layout = QFormLayout(group)
        for d in range(1,20):
            radio = QRadioButton()
            radio.setText(str(d))
            layout.addWidget(radio)
        scroll.setWidget(group)

        hlayout = QHBoxLayout()
        hlayout.addWidget(scroll)
        dialog.setLayout(hlayout)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

        dialog.exec_()
myapp = QApplication(sys.argv)
window = Window()

myapp.exec_()
sys.exit()