import os

from PySide2 import QtCore
from PySide2.QtCore import QUrl
from PySide2.QtWebEngineWidgets import QWebEngineSettings, QWebEngineView
from PySide2.QtWidgets import *
import sys
from PySide2.QtGui import QIcon, QFont

import eel
from flask import Flask, render_template, jsonify

app = Flask(__name__)


class Window(QWidget):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        self.setWindowTitle("About")
        self.setGeometry(300, 200, 866, 446)
        # self.setMaximumWidth(700)
        # self.setMinimumWidth(700)

        self.btn = QPushButton(self,"Web")
        self.btn.clicked.connect(self.btn_clicked)

    @app.route('/')
    def btn_clicked(self):
        return render_template('index.html')
        print("test")

    @app.route('/_get_data/', methods=['POST'])
    def _get_data(self):
        myList = ['Element1', 'Element2', 'Element3']

        return jsonify({'data': render_template('response.html', myList=myList)})
        print("test1")


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

