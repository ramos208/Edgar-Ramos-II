from PySide2 import QtCore
from PySide2.QtWidgets import *
import sys
from PySide2.QtGui import QIcon, QFont




class Window(QWidget):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        self.setWindowTitle("About")
        self.setGeometry(300, 200, 866, 446)
        # self.setMaximumWidth(700)
        # self.setMinimumWidth(700)

        self.setIcon()

        self.createLayout()

        gbox = QHBoxLayout()
        gbox.addWidget(self.groupBox)
        gbox.addWidget(self.r_groupBox)
        self.setLayout(gbox)

        self.show()



    def setIcon(self):
        appIcon = QIcon("icon.png")
        self.setWindowIcon(appIcon)

    def createLayout(self, parent=None):
        self.r_groupBox = QGroupBox()


        r_vbox = QVBoxLayout()
        self.r_groupBox.setLayout(r_vbox)
        self.r_groupBox.setStyleSheet(
            'QGroupBox {background-image: url("about_navis2.png"); background-repeat: no-repeat;}')

        self.groupBox = QGroupBox()
        self.groupBox.setStyleSheet(
            'QGroupBox {background-image: url("left_about.png"); background-repeat: no-repeat;}'
            'QPushButton{font-size:15px; background-color : #013461; color:white; font-weight:bold;}'
            'QPushButton:focus,QPushButton:hover{background-color: #0b89f6;}')
        self.groupBox.setFont(QFont("Sanserif", 15))
        self.groupBox.setMaximumWidth(220)
        self.groupBox.setMinimumWidth(220)
        vbox = QVBoxLayout()

        btn_about = QPushButton("About Navis", self)
        btn_about.setMinimumHeight(40)
        btn_about.clicked.connect(self.btn_about_clicked)

        btn_develop = QPushButton("The Team", self)
        btn_develop.setMinimumHeight(40)
        btn_develop.clicked.connect(self.btn_develop_clicked)

        btn_partner = QPushButton("Collaborations", self)
        btn_partner.setMinimumHeight(40)
        btn_partner.clicked.connect(self.btn_partner_clicked)

        btn_its = QPushButton("About ITS", self)
        btn_its.setMinimumHeight(40)
        btn_its.clicked.connect(self.btn_its_clicked)

        label_logo = QLabel('Navis',self)
        label_logo.setStyleSheet('color:transparent')

        vbox.addWidget(btn_about)
        vbox.addWidget(btn_its)
        vbox.addWidget(btn_develop)
        vbox.addWidget(btn_partner)
        vbox.addWidget(label_logo)
        self.groupBox.setLayout(vbox)
    def btn_its_clicked(self):
        self.r_groupBox.setStyleSheet(
            'QGroupBox {background-image: url("about_its.png"); background-repeat: no-repeat;}')

    def btn_about_clicked(self):
        self.r_groupBox.setStyleSheet(
            'QGroupBox {background-image: url("about_navis2.png"); background-repeat: no-repeat;}')

    def btn_develop_clicked(self):
        self.r_groupBox.setStyleSheet(
            'QGroupBox {background-image: url("about_develop.png"); background-repeat: no-repeat;}')
    def btn_partner_clicked(self):
        self.r_groupBox.setStyleSheet(
            'QGroupBox {background-image: url("about_partner.png"); background-repeat: no-repeat;}')

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

