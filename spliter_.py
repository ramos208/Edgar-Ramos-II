#
import sys
from PySide2 import QtGui, QtCore
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QWidget, QHBoxLayout, QFrame, QApplication, QStyleFactory, QSplitter, QDockWidget, \
    QMainWindow, QGroupBox, QButtonGroup, QLabel, QPushButton, QRadioButton
from View.dock_widgets.m_test_dock import TestDock

class Example(QMainWindow):

    def __init__(self):
        super(Example, self).__init__()

        self.setGeometry(QApplication.desktop().availableGeometry().x(),
                         QApplication.desktop().availableGeometry().y(),
                         QApplication.desktop().availableGeometry().width(),
                         QApplication.desktop().availableGeometry().height())

        self.initUI()


    def initUI(self):
        hbox = QHBoxLayout(self)

        topleft = QWidget(self)
        # topleft.setCheckable(True)
        # topleft.setCursor(Qt.PointingHandCursor)
        # topleft.toggled.connect(lambda: self.test_(topleft))
        # topleft.clicked.connect(lambda: self.test_(topleft))
        topleft.setCursor(Qt.PointingHandCursor)
        # groupbtn = QButtonGroup()
        # label = QRadioButton('asdasdasdasdasd')
        # label2 = QRadioButton('asdasdasdasdasd')
        #
        # layout.addWidget(label)
        # layout.addWidget(label2)
        #
        # groupbtn.addButton(label)
        # groupbtn.addButton(label2)
        # groupbtn.setExclusive(True)
        # groupbtn.buttonClicked.connect(self.test_)

        # topleft.setFrameShape(QFrame.StyledPanel)
        # topleft.setStyleSheet('background-color:#000;')
        topright = QWidget(self)
        topright.setStyleSheet('background-color:red;')

        top2left = QWidget(self)
        # topleft.setFrameShape(QFrame.StyledPanel)
        top2left.setStyleSheet('background-color:blue;')
        top2left.resize(200,700)

        top2right = QWidget(self)
        top2right.setStyleSheet('background-color:red;')
        # top2right.resize(100,500)

        top3left = QWidget(self)
        # top3left.resize(10,100)
        # topleft.setFrameShape(QFrame.StyledPanel)
        top3left.setStyleSheet('background-color:red;')
        top3right = TestDock(self)
        # top3right.resize(1,1)
        # top3right.setStyleSheet('background-color:red;')

        # topright.setFrameShape(QFrame.StyledPanel)

        splitter13 = QSplitter(Qt.Vertical)
        splitter13.addWidget(top3left)
        splitter13.addWidget(top3right)
        # splitter13.resize(200, 100)
        # bottom.setFrameShape(QFrame.StyledPanel)

        splitter1 = QSplitter(Qt.Vertical)
        splitter1.addWidget(topleft)
        splitter1.addWidget(topright)
        splitter1.resize(200,100)

        splitter12 = QSplitter(Qt.Vertical)
        splitter12.addWidget(top2left)
        splitter12.addWidget(top2right)
        # splitter12.resize(100, 100)

        splitter2 = QSplitter(Qt.Horizontal)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(splitter13)
        splitter2.addWidget(splitter12)

        hbox.addWidget(splitter2)
        widget= QFrame()
        widget.setLayout(hbox)
        self.setCentralWidget(widget)
        QApplication.setStyle(QStyleFactory.create('Cleanlooks'))

        self.setWindowTitle('QtGui.QSplitter')
        self.show()

    def test_(self,ctrl):
        print('click test')
    def onChanged(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()


# import requests
# request = requests.get('https://downloads.mongodb.com/compass/mongodb-compass-1.21.2-win32-x64.exe')
# print(request.status_code)
# if request.status_code == 200:
#     print('Web site exists')
# else:
#     print('Web site does not exist')

# import urllib
# from urllib.error import HTTPError, URLError
# from urllib.request import urlopen
#
# try:
#     urlopen('https://downloads.mongodb.com/compass/mongodb-compass-1.21.2-win32-x64.exe2')
# except HTTPError as e:
#     print(e.code)
# except URLError as e:
#     print(e.args)

# data = ['Login','Create Account','Update Password','Add Region','Delete Account','Edit Account','Update Related Account','Change Name','Version Update'
# ]
#
# print(sorted(data))

# f = ['2020', '10', '07']
# t = ['2020', '11', '20']
# # f = ['2020/10/20']
# # t = ['2020/11/20']
# # t = ['2020/12/20','2020/10/20','2020/11/20']
# date_ = []
# f_date = []
# for d in range(1,31):
#     f_date.append(d)
# for d in range(int(f[2]),32):
#     if int(t[2]) >= d:
#         date_.append(d)
# print(date_)
# print(f_date)
# if f[0] < t[0] and f[1] < t[1]:
#     print('ok')
# elif f[0] == t[0] and f[1] == t[1] and t[2] in date_:
#     print('equal')
#
# from datetime import date, timedelta
# start_date = str(date.today()).split('-')
# end_date = date(2020, 10, 1)
#
# # print(start_date == end_date)
# # delta = timedelta(days=1)
# # while start_date <= end_date:
# #     print (start_date.strftime("%Y-%m-%d"))
# #     start_date += delta
# #
#
# print(start_date)


# data = "['MASBATE', ' ROMBLON 123']"
# a = data[1:-1].replace("'",'')
# print(a)
# for d in a.split(','):
#     print(d.strip())