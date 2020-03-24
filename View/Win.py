import os

from PySide2.QtCore import QUrl
from PySide2.QtGui import QFont, QIcon
from PySide2.QtWebEngineWidgets import QWebEngineView, QWebEngineSettings
from PySide2.QtWidgets import QApplication, QWidget, QDialog, QHBoxLayout, QGroupBox, QVBoxLayout, QPushButton
import sys

class Window(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Login")
        # self.setGeometry(300,300,300,400)

        # self.setGeometry(300,300,300,400)

        # self.setMinimumHeight(500)
        # self.setMinimumWidth(300)
        # self.setMaximumHeight(500)
        # self.setMaximumWidth(300)
        # self.province_name = name
        # print(name)
        self.setWindowTitle("City Map - Terminal")
        # self.setGeometry(300, 200, 1200, 800)
        self.resize(1200, 800)

        self.unit_ui()
        Hbox = QHBoxLayout()
        Hbox.addWidget(self.VLgroupBox)
        Hbox.addWidget(self.VRgroupBox)
        self.setLayout(Hbox)

        # map = QWebEngineView(self)
        # map.settings().setAttribute(QWebEngineSettings.JavascriptEnabled, True)
        # map.load(QUrl.fromLocalFile(dir.map_city_dir))

    def unit_ui(self):
        self.VLgroupBox = QGroupBox()
        self.VLgroupBox.setFont(QFont("Sanserif", 13))
        self.VLgroupBox.setMinimumWidth(350)
        self.VLgroupBox.setMaximumWidth(350)

        self.VRgroupBox = QGroupBox()

        VLbox = QVBoxLayout()
        VRbox = QVBoxLayout()

        button = QPushButton("CSS", self)
        button.setIcon(QIcon("css.png"))
        button.setMinimumHeight(40)
        VLbox.addWidget(button)

        button1 = QPushButton("C++", self)
        button1.setIcon(QIcon("cpp.png"))
        button1.setMinimumHeight(40)
        VLbox.addWidget(button1)

        button2 = QPushButton("Javascript", self)
        button2.setIcon(QIcon("javascript.png"))
        button2.setMinimumHeight(40)
        VLbox.addWidget(button2)

        map_city_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../index2.html'))
        map = QWebEngineView(self)
        map.settings().setAttribute(QWebEngineSettings.JavascriptEnabled, True)
        map.load(QUrl.fromLocalFile(map_city_dir))
        # map.setHtml(dir.map_city_dir)

        print(map_city_dir)

        VRbox.addWidget(map)

        self.VRgroupBox.setLayout(VRbox)
        self.VLgroupBox.setLayout(VLbox)

# def Start():
#     myApp = QApplication(sys.argv)
#     window = Window()
#     window.show()
#
#     # time.sleep(5)
#     window.resize(300, 500)
#
#     myApp.exec_()
#     sys.exit(0)
#
# Start()
