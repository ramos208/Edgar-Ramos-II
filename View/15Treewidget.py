from PySide2.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QCheckBox, QTreeWidget, QTreeWidgetItem, \
    QAbstractItemView
import sys
from PySide2.QtGui import QIcon
from PySide2.QtCore import Qt


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Pyside2 QCheckBox")
        self.setGeometry(300, 200, 400, 100)

        self.setIcon()

        self.createCheckBox()

        self.show()

    def setIcon(self):
        appIcon = QIcon("icon.png")
        self.setWindowIcon(appIcon)

    def createCheckBox(self):

        vessels_data_style = 'QLabel{font-size:22px; font-weight:bold;color : #003461;}' \
                             'QLineEdit{font-size:15px;background-color:#f8f6f6; color:#18476f; border: 1.5px solid; border-radius: 5px; padding:5px; border-color:#18476f;}' \
                             'QComboBox{font-size:15px;background-color:#f8f6f6; color:#18476f; border: 1.5px solid; border-radius: 5px; padding:5px;' \
                             'border-color:#18476f;}' \
                             'QComboBox QAbstractItemView {padding:5px; background-color:white;}' \
                             'test_QComboBox QAbstractItemView {border: 2px solid darkgray;selection-background-color: lightgray;color:rgb(87,117,131);}' \
                             'QListWidget{font-size:22px;background-color:#f8f6f6; color:#18476f; border: 1.5px solid; border-radius: 5px; padding:15px; margin:10px;border-color:#18476f;}' \
                             'QTableWidget{background-color:#f8f6f6; color:#18476f; border: 1.5px solid; border-radius: 5px; padding:5px; border-color:#18476f;}' \
                             'QScrollBar{background-color:qlineargradient(x1:0, y1:0, x2:0, y2:1,stop:1 #003461, stop:0 #0092d1);}' \
                             'QHeaderView::section {background-color:#18476f; color:white; font-weight: bold; border-radius: 3px; padding:5px; }' \
                             'QPushButton{background-color:#18476f; color:#ffffff;border: 1.5px solid; border-radius: 10px; padding:5px; font-size:18px; font-weight:bold; border-color:#18476f;}' \
                             'QPushButton:hover{background-color:#086abe;}' \
                             'QPushButton:focus{border-color: #0b89f6;}'

        vbox = QVBoxLayout()

        self.tree = QTreeWidget()
        self.tree.setMinimumHeight(300)
        # self.tree_master_db.setStyleSheet(vessels_data_style)
        self.tree.setSelectionMode(QAbstractItemView.ExtendedSelection)
        # self.tree_master_db.setHeaderHidden(True)

        vbox.addWidget(self.tree)
        self.setLayout(vbox)

        self.populate()
    def populate(self):
        headers = ['Port', 'Vessel type']
        self.tree.setColumnCount(len(headers))
        self.tree.setHeaderLabels(headers)

        data_values = [['test', 'asdasdsad'],['1test', 'asdasdsad1']]

        for d in data_values:
            tree_widget_item = QTreeWidgetItem(d)
            self.tree.addTopLevelItem(tree_widget_item)
            self.tree.setItemSelected(tree_widget_item, True)
        # self.tree.setStyleSheet(vessels_data_style)

        for column in range(self.tree.columnCount()):
            self.tree.resizeColumnToContents(column)

        self.tree.setSortingEnabled(True)
        self.tree.sortItems(0, Qt.AscendingOrder)

    def checkBoxChange(self, state):
        if state == Qt.Checked:
            self.label.setText("Yes I Like Football")

        else:
            self.label.setText("No I Dont Like Football")


myapp = QApplication(sys.argv)
window = Window()
myapp.exec_()
sys.exit()