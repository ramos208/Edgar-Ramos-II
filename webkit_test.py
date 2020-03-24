import os

from PySide2 import QtCore
from PySide2.QtCore import Slot, QUrl
from PySide2.QtWebEngineWidgets import *
from PySide2.QtWidgets import QWidget, QApplication
from __future__ import print_function	# For Py2/3 compatibility
import eel

html = """
<html>
<body>
    <h1>Hello!</h1><br>
    <h2><a href="#" onclick="printer.text('edgar')">QObject Test</a></h2>
    <h2><a href="#" onclick="printer.test2">Test</a></h2>
    <h2><a href="#" onclick="alert('Javascript works!')">JS test</a></h2>
</body>
</html>
"""

html2 = """+"""


# class ConsolePrinter(QWidget):
#     def __init__(self, parent=None):
#         super(ConsolePrinter, self).__init__(parent)
#
#     @Slot(str)
#     def text(self, message):
#         print(message)
#
#     @Slot(str)
#     def test(self,m):
#         print(m)
#         app2 = QtGui.QMainWindow()
#         app2.setGeometry(300, 300, 250, 150)
#         app2.show()
#         # app2.exec_()

class appo(QWidget):
    def __init__(self):
        super(appo, self).__init__()
        self.show()

        view = QWebEngineView(self)
        frame = view.page()

        # printer = ConsolePrinter()
        _dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'webkit.html'))

        view.settings().setAttribute(QWebEngineSettings.JavascriptEnabled, True)
        # view.load(QUrl.fromLocalFile(_dir))
        view.setGeometry(QtCore.QRect(10, 10, 1000, 500))
        view.setHtml(html)
        t = self

        # frame.runJavaScript()
        frame.runJavaScript("printer",self)
        # frame.runJavaScript(self)
        # frame.evaluateJavaScript("alert('Hello');")
        # frame.evaluateJavaScript("printer.text('Goooooooooo!');")
        view.show()
        # frame.evaluateJavaScript("printer.test;")
        # self.test2()

    # @Slot(str)
    def test2(self):
        from View import Win
        self.Sw = Win.Window()
        self.Sw.show()


    @Slot(str)
    def text(self, message):
        # print(message)
        self.test2()

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    db = None
    MW = appo()
    MW.show()
    sys.exit(app.exec_())

    # import sys
    # app = QApplication(sys.argv)
    #
    # view = QWebView()
    # frame = view.page().mainFrame()
    # printer = ConsolePrinter()
    #
    # view.setHtml(html)
    # frame.addToJavaScriptWindowObject('printer', printer)
    # frame.evaluateJavaScript("alert('Hello');")
    # frame.evaluateJavaScript("printer.text('Goooooooooo!');")
    # # frame.evaluateJavaScript("printer.test;")
    # view.show()
    # # app.exec_()
    # sys.exit(app.exec_())