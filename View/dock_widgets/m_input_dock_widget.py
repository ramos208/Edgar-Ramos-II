"""/*********************************************************************
                        Router Selector Dock Widget
                        ===========================
The Route selector section allows the user to define the route to be analyzed by selecting the origin port and the destination port.
This means that the user aims to analyze the route capacity from the origin port to the destination port.
For this prototype version

**************************************************************************/"""
import os

from PySide2.QtGui import QIcon
from PySide2.QtWidgets import *
from PySide2.QtCore import *


class MInputDock(QDockWidget):

    origin_changed = Signal(str)
    destination_changed = Signal(str)
    def __init__(self, parent, gc, db):
        super(MInputDock, self).__init__(parent=parent)

        # self.setMaximumWidth(480)
        self.setWindowTitle('Route selector')
        self.setFloating(False)
        # self.setFeatures(QDockWidget.DockWidgetFloatable | QDockWidget.DockWidgetMovable)
        self.setFeatures(QDockWidget.NoDockWidgetFeatures)
        self.parent = parent
        self.gc = gc
        self.db = db

        frame = QFrame()
        layout = QVBoxLayout(frame)
        self.setWidget(frame)

        route_select_groupbox = QGroupBox()
        route_select_layout = QFormLayout(route_select_groupbox)

        self.origin_combobox = QComboBox()
        self.origin_combobox.addItem('None')
        # self.origin_combobox.currentTextChanged.connect(self._origin_port_changed)
        self.origin_combobox.setMinimumContentsLength(10)
        self.origin_combobox.setItemDelegate(QStyledItemDelegate())

        self.destination_combobox = QComboBox()
        self.destination_combobox.addItem('None')
        # self.destination_combobox.currentTextChanged.connect(self._destination_port_changed)
        self.destination_combobox.setMinimumContentsLength(10)
        self.destination_combobox.setItemDelegate(QStyledItemDelegate())

        self.error_msg = QLabel('Error', self)
        self.error_msg.setStyleSheet('color:red; font-size:12px;')
        self.error_msg.hide()

        title_ = QLabel('Select route', self)
        route_select_layout.addRow(title_)
        route_select_layout.addRow('Origin port:', self.origin_combobox)
        route_select_layout.addRow('Destination port:', self.destination_combobox)
        route_select_layout.addWidget(self.error_msg)

        route_details_groupbox = QGroupBox()

        route_details_layout = QFormLayout(route_details_groupbox)

        self.name_input = QLineEdit()
        self.distance_input = QLineEdit()
        # self.distance_input.textChanged.connect(self.distance_input_change)
        self.service_hours_input = QLineEdit()
        # self.service_hours_input.textChanged.connect(self.service_hours_input_change)

        self.error_distance = QLabel('Enter a valid positive number only',self)
        self.error_distance.hide()

        self.error_hour = QLabel('Enter a valid time frame 1 to 24 hours ')
        self.error_hour.hide()

        # self.name_input.setReadOnly(True)
        title_ = QLabel('Route details', self)
        route_details_layout.addRow(title_)
        route_details_layout.addRow('Name:', self.name_input)
        self.name_input.setDisabled(True)
        route_details_layout.addRow('Distance (NM):', self.distance_input)
        route_details_layout.addWidget(self.error_distance)
        route_details_layout.addRow('Operating hours per day (h):', self.service_hours_input)
        route_details_layout.addWidget(self.error_hour)

        layout.addWidget(route_select_groupbox)
        layout.addWidget(route_details_groupbox)
        layout.addStretch(1)


