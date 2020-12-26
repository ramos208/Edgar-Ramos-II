from PySide2.QtWidgets import *

__author__ = 'Caroline Beyne'

from PySide2 import QtGui, QtCore
import sys
from FrameLayout import FrameLayout

if __name__ == '__main__':

    app = QApplication(sys.argv)

    win = QMainWindow()
    w = QWidget()
    w.setMinimumWidth(350)
    win.setCentralWidget(w)
    l = QVBoxLayout()
    l.setSpacing(0)
    l.setAlignment(QtCore.Qt.AlignTop)
    w.setLayout(l)

    t = FrameLayout(title="Buttons")
    t.addWidget(QPushButton('a'))
    t.addWidget(QPushButton('b'))
    t.addWidget(QPushButton('c'))

    f = FrameLayout(title="TableWidget")
    rows, cols = (6, 3)
    data = {'col1': ['1', '2', '3', '4', '5', '6'],
            'col2': ['7', '8', '9', '10', '11', '12'],
            'col3': ['13', '14', '15', '16', '17', '18']}
    table = QTableWidget(rows, cols)
    headers = []
    for n, key in enumerate(sorted(data.keys())):
        headers.append(key)
        for m, item in enumerate(data[key]):
            newitem = QTableWidgetItem(item)
            table.setItem(m, n, newitem)
    table.setHorizontalHeaderLabels(headers)
    f.addWidget(table)

    l.addWidget(t)
    l.addWidget(f)

    win.show()
    win.raise_()

    sys.exit(app.exec_())

