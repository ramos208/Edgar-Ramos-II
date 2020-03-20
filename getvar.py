import sys
import PySide2
from PySide2.QtWidgets import QLineEdit, QVBoxLayout, QWidget, QApplication

html = '''
<html><head>
<meta name="viewport" content="initial-scale=1.0, user-scalable=no" />
<style type="text/css">
    html { height: 100% }
    body { height: 100%; margin: 0; padding: 0 }
    #map { width: 100%; height: 100% }
</style>
<script src="https://maps.googleapis.com/maps/api/js"></script>
<script type="text/javascript">
    var map, marker
    function initialize() {
        map = new google.maps.Map(document.getElementById("map"), {
            center: {lat: 40.793697, lng: -77.8586},
            zoom: 10
        })
        marker = new google.maps.Marker({
            map: map,
            position: map.getCenter(),
            draggable: true
        })
        marker.addListener("dragend", function () {
            var pos = marker.getPosition()
            qt.showLocation(pos.lat(), pos.lng())
            console.log("dragend: " + pos.toString())
        })
    }
    google.maps.event.addDomListener(window, "load", initialize)
</script>
</head>
<body><div id="map"/></body>
</html>
'''

class WebPage(QWebView):
    def javaScriptConsoleMessage(self, message, line, source):
        if source:
            print('line(%s) source(%s): %s' % (line, source, message))
        else:
            print(message)

class Proxy(PySide2.QtCore.QObject):
    @PySide2.QtCore.Slot(float, float)
    def showLocation(self, latitude, longitude):
        self.parent().edit.setText('%s, %s' % (latitude, longitude))

class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.view = QWebView(self)
        self.view.setPage(WebPage(self))
        self.edit = QLineEdit(self)
        layout = QVBoxLayout(self)
        layout.addWidget(self.view)
        layout.addWidget(self.edit)
        self.map = self.view.page().mainFrame()
        self.map.loadFinished.connect(self.handleLoadFinished)
        self.view.setHtml(html)
        self._proxy = Proxy(self)

    def handleLoadFinished(self, ok):
        self.map.addToJavaScriptWindowObject('qt', self._proxy)

if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = MainWindow()
    window.setGeometry(500, 300, 800, 600)
    window.show()
    sys.exit(app.exec_())