import sys
from PySide2 import QtCore, QtGui
from PySide2.QtWidgets import QWidget, QScrollArea, QVBoxLayout, QFrame, QApplication, QLabel, QFormLayout, QGroupBox


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)
        layout = QVBoxLayout(self)
        layout.addWidget(self.scroll)
        widget = QGroupBox()
        widget.setStyleSheet('QWidget::hover{'
                               'background-color:#f8f6f6; '
                               'color:#18476f;'
                               'border: 0.5px solid;'
                               'border-radius: 2px; '
                               'padding: 2px;'
                               'border-color:#18476f;}')
        widget.setMouseTracking(True)
        layout = QVBoxLayout(widget)
        layout.setContentsMargins(0,0,0,0)
        # for text in 'red green yellow purple orange blue'.split():
        #     item = QFrame()
        #     item.setObjectName(text)
        #     item.setStyleSheet('background-color: %s' % text)
        #     layout.addWidget(item)

        test = QWidget()
        test.setObjectName('test2')
        # test.setStyleSheet('*:hover {background: red}')
        test_layout = QFormLayout(test)
        test_layout.setContentsMargins(0,0,0,0)
        lbl = QLabel('yeeyery')
        lbl2 = QLabel('yeeyery333')
        # lbl.setObjectName('test')
        # lbl2.setObjectName('test')
        test_layout.addRow('test',lbl)
        test_layout.addRow('test',lbl2)

        # test.setObjectName('test')

        layout.addWidget(test)
        self.scroll.setWidget(widget)
        self._lastpos = None

    # def mouseMoveEvent(self, event):
    #     self._lastpos = event.pos()
    #     widget = self.childAt(event.pos())
    #     if (widget is not None and self._lastpos is not None and
    #             widget is self.childAt(self._lastpos)):
    #         if widget.objectName():
    #             print('move:', widget.objectName())

    def mousePressEvent(self, event):
        self._lastpos = event.pos()

    def mouseReleaseEvent(self, event):
        widget = self.childAt(event.pos())
        if (widget is not None and self._lastpos is not None and
            widget is self.childAt(self._lastpos)):
            if widget.objectName():
                print('click:', widget.objectName())
        self._lastpos = None
    #
    # def mouseDoubleClickEvent(self, event):
    #     widget = self.childAt(event.pos())
    #     if widget is not None and widget.objectName():
    #         print('dblclick:', widget.objectName())

if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = Window()
    window.setGeometry(600, 100, 300, 400)
    window.show()
    sys.exit(app.exec_())