import sys

from PySide2 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets, QtWebChannel
from PySide2.QtCore import Slot


class WebEnginePage(QtWebEngineWidgets.QWebEnginePage):
    pass

class AppManager(QtCore.QObject):
    textChanged = QtCore.Signal(str)
    # test2 = QtCore.Signal(str)
    def __init__(self, webview):
        QtCore.QObject.__init__(self)
        self.m_text = ""
        # timer = QtCore.QTimer(self)
        # timer.timeout.connect(self.on_timeout)
        # timer.start(1000)

    def on_timeout(self):
        self.text  = QtCore.QDateTime.currentDateTime().toString()

    @QtCore.Property(str, notify=textChanged)
    def text(self):
        print("test ========================")
        return self.m_text
        # print("edgar")
        # print("=============================")

    @text.setter
    def setText(self, text):
        if self.m_text == text:
            return
        self.m_text = text
        self.textChanged.emit(self.m_text)
        print(self.m_text)

    # @QtCore.Property(str, notify=test2)
    @Slot(str)
    def test2(self,x):
        print(x)
        # self.m_text="ramos"
        # self.textChanged.emit(self.m_text)
        # from View import Win
        # self.Sw = Win.Window()
        # self.Sw.exec_()




class WebView(QtWebEngineWidgets.QWebEngineView):
    def __init__(self, parent=None):
        QtWebEngineWidgets.QWebEngineView.__init__(self, parent)
        self.setPage(WebEnginePage(self))

    def contextMenuEvent(self, event):
        pass


class AppWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.view = WebView(self)
        self.page = self.view.page()
        self.app_manager = AppManager(self.view)
        channel = QtWebChannel.QWebChannel(self)
        self.page.setWebChannel(channel)
        channel.registerObject("app_manager", self.app_manager)
        self.view.load(QtCore.QUrl.fromLocalFile(QtCore.QDir.current().filePath("index2.html")))
        self.setCentralWidget(self.view)
        m = "edag"
        # self.page.runJavaScript(self.app_manager.test2)
        # self.test2()

    def test2(self):
        from View import Win
        self.Sw = Win.Window()
        self.Sw.show()

    @Slot(str)
    def text(self, message):
        # print(message)
        self.test2()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = AppWindow()
    w.show()
    sys.exit(app.exec_())