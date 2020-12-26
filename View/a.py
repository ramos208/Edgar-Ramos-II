import os

from PySide2 import QtCore, QtWebChannel
from PySide2.QtGui import QIcon, QFont
from PySide2.QtWebEngineWidgets import QWebEngineView, QWebEngineSettings
from PySide2.QtWidgets import *
from PySide2.QtCore import *

class CityMapPopup(QDialog):

    def __init__(self, parent,db,name):
        super(CityMapPopup, self).__init__()

        self.province_name = name
        print(name)
        self.setWindowTitle("City Map - Terminal")
        # self.setGeometry(300, 200, 1200, 800)
        self.resize(1200,800)

        self.unit_ui(self.province_name)


        self.HBox = QGroupBox("test")
        # self.HBox.setStyleSheet(style.style_groupbox)
        Hbox = QHBoxLayout()
        Hbox.addWidget(self.VLgroupBox)
        self.HBox.setLayout(Hbox)

        # Vbox = QVBoxLayout()
        # Vbox.addWidget(self.HBox)

        # self.setLayout(Vbox)

    def unit_ui(self,name):

        self.VLgroupBox = QGroupBox("test")
        self.VLgroupBox.setFont(QFont("Sanserif", 25))
        self.VLgroupBox.setStyleSheet('QListWidget{border-color:transparent;}')
        self.VLgroupBox.setMinimumWidth(350)
        self.VLgroupBox.setMaximumWidth(350)

        VLbox = QVBoxLayout()
        VRbox = QVBoxLayout()

        # groupbox layout
        land_type = ['Car', 'Taxi', 'Van/Bus', 'Motorcycle', 'Bicycle', 'Walking']
        maritime_type = ['Ferry', 'Roro', 'Cruise']
        textedit_max_height = 35
        textedit_min_width = 100
        self.combo_land_type = QComboBox()
        self.combo_land_type.addItems(land_type)
        # self.origin_combobox.currentTextChanged.connect(self._origin_port_changed)
        self.combo_land_type.setMinimumContentsLength(20)
        self.combo_land_type.setItemDelegate(QStyledItemDelegate())

        self.land_fare = QTextEdit()
        self.land_fare.setMinimumWidth(textedit_min_width)
        self.land_fare.setMaximumHeight(textedit_max_height)
        # self.land_fare.currentTextChanged.connect(self._destination_port_changed)

        self.land_speed = QTextEdit()
        self.land_speed.setMinimumWidth(textedit_min_width)
        self.land_speed.setMaximumHeight(textedit_max_height)

        VLbox.addWidget(self.combo_land_type)
        VLbox.addWidget(self.land_fare)
        VLbox.addWidget(self.land_speed)
        self.VLgroupBox.setLayout(VLbox)




if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    db = None
    name = "test ui"
    MW = CityMapPopup(app,db,name)
    MW.show()
    sys.exit(app.exec_())

