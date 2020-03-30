import os

from PySide2.QtCore import QUrl
from PySide2.QtWebEngineWidgets import QWebEngineView, QWebEngineSettings
from PySide2.QtWidgets import *
import sys
from PySide2.QtGui import QIcon, QFont




class Window(QWidget):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        self.setWindowTitle("Layout Managment")
        self.setGeometry(300,100, 700,700)

        map_city_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'routing.html'))

        web = QWebEngineView(self)
        web.settings().setAttribute(QWebEngineSettings.JavascriptEnabled, True)
        # web.page().certificateError()

        print(map_city_dir)
        web.load(QUrl.fromLocalFile(map_city_dir))

        # web.load(QUrl.fromLocalFile(map_city_dir))
        # web.setContent(map_city_dir)

        web.setGeometry(0, 0, 700, 700)

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    MW = Window()
    MW.show()
    sys.exit(app.exec_())

