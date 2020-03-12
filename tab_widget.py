from PySide2.QtWidgets import *


class TabWidget(QTabWidget):
    def __init__(self, parent=None):
        super(TabWidget, self).__init__(parent=parent)

        self.parent = parent
        # self.setTabsClosable(True)
