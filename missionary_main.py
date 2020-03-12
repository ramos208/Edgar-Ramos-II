from PySide2 import QtCore
from PySide2.QtCore import Qt
from PySide2.QtWidgets import *
import sys
from PySide2.QtGui import QIcon, QFont
from View.dock_widgets.m_input_dock_widget import MInputDock
from View.tabs.m_gis_tab import MGISMap
from tab_widget import TabWidget


class Missionary(QMainWindow):
    def __init__(self, parent, db):
        super(Missionary, self).__init__()

        self.db = db

        self.gc = None
        self.engine = None
        self.tab_widget = None
        self.data_visual_tab = None
        self.engine_thread = None
        self.db_manager = None
        self.acc_manager = None
        self.query_thread = None

        self.setGeometry(QApplication.desktop().availableGeometry().x(),
                         QApplication.desktop().availableGeometry().y(),
                         QApplication.desktop().availableGeometry().width(),
                         QApplication.desktop().availableGeometry().height())

        self.setWindowTitle("Missionary Route")
        self.menu_bar = self.menuBar()
        self.menu_bar.setNativeMenuBar(False)
        # self.menu_bar.setStyleSheet(style_main_menu_bar)

        self.toolbar = QToolBar('Toolbar', parent=self)
        self.toolbar.setMovable(False)
        self.addToolBar(self.toolbar)

        self.status_bar = QStatusBar(self)
        self.setStatusBar(self.status_bar)

        file_menu = QMenu('File')

        run_action = QAction('Run', self)  # Run Button
        # icon = QIcon(os.path.join(dir.icon__toolbar_dir, dir.img_toolbar_play))
        # run_action.setIcon(icon)
        run_action.setShortcut('Ctrl+R')
        run_action.setStatusTip("Run")
        run_action.triggered.connect(self.run)

        file_menu.addAction(run_action)
        self.menu_bar.addMenu(file_menu)

        self.toolbar.addAction(run_action)

        """Dock Widget"""
        self.m_input_dock_widget = MInputDock(self, self.gc, self.db)
        self.addDockWidget(Qt.LeftDockWidgetArea, self.m_input_dock_widget)

        """Tab Widget"""
        frame = QFrame()
        layout = QGridLayout(frame)
        self.setCentralWidget(frame)

        # self.gc = MGISMap(self)

        self.tab_widget = QTabWidget(self)
        self.m_gis_tab = MGISMap(self)
        self.tab_widget.addTab(self.m_gis_tab,'Map')

        layout.addWidget(self.tab_widget)


    def run(self):
        pass

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    db = None
    MW = Missionary(app,db)
    MW.show()
    sys.exit(app.exec_())
