"""/*********************************************************************
                        Data Visualization Tab
                        ===========================
This file provide the graphical representation of information and data base
on Output Data Dock

**************************************************************************/"""
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from PySide2.QtCharts import QtCharts


class MGISMap(QWidget):
    def __init__(self, parent):
        super(MGISMap, self).__init__(parent=parent)
        self.parent = parent

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.chart = None
        self.chart_view = QtCharts.QChartView()
        self.chart_view.setRenderHint(QPainter.Antialiasing)

        self.layout.addWidget(self.chart_view)

        self.roro_bar_sets = None
        self.nonroro_bar_sets = None

        self.roro_vessels = None
        self.nonroro_vessels = None

        self.roro_output = None
        self.nonroro_output = None



    def generate_chart(self, roro_vessels, nonroro_vessels, roro_output, nonroro_output, time_frame, type_):
        """
        Generate Chart For Overview
        :param roro_vessels:
        :param nonroro_vessels:
        :param roro_output:
        :param nonroro_output:
        :param time_frame:
        :param type_:
        :return:
        """
        self.roro_vessels = roro_vessels
        self.nonroro_vessels = nonroro_vessels
        self.roro_output = roro_output
        self.nonroro_output = nonroro_output

        if time_frame == 'Overview':
            self.create_overview_chart(type_)
        else:
            self.create_month_chart(time_frame.upper(), type_)

        self.connect_legend_markers()

    def create_overview_chart(self, type_):
        """
        Generate what type of vessel
        :param type_: roro or nonroro
        :return:
        """

        months = ['JANUARY', 'FEBRUARY', 'MARCH', 'APRIL', 'MAY', 'JUNE', 'JULY', 'AUGUST', 'SEPTEMBER', 'OCTOBER',
                  'NOVEMBER', 'DECEMBER']

        max_ = 0.0
        bar_series = None
        line_series = None

        if type_ == 'All types':
            self.chart = QtCharts.QChart()
            self.chart.setTheme(QtCharts.QChart.ChartThemeBlueCerulean)

            # RORO DATA
            self.roro_bar_sets = dict()
            for vessel_name in self.roro_vessels:
                self.roro_bar_sets[vessel_name] = BarSet(vessel_name)

            for roro_name, bar_set in self.roro_bar_sets.items():
                data = []

                for month in months:
                    if month in self.roro_output and roro_name in self.roro_output[month] and \
                            self.roro_output[month][roro_name]:
                        profit = self.roro_output[month][roro_name]['total profit']
                        if 'vessels required' in self.roro_output[month][roro_name]:
                            vessels_required = self.roro_output[month][roro_name]['vessels required']
                            data.append(profit / vessels_required)
                        else:
                            data.append(profit)
                    else:
                        data.append(0.0)

                max_ = max(max_, max(data))
                bar_set.append(data)

            bar_series = QtCharts.QBarSeries()
            for bar_set in self.roro_bar_sets.values():
                bar_series.append(bar_set)

            self.chart.addSeries(bar_series)

            # NONRORO DATA
            line_series = dict()
            for vessel_name in self.nonroro_vessels:
                series = QtCharts.QLineSeries()
                series.setName(vessel_name)
                line_series[vessel_name] = series

            for vessel_name, series in line_series.items():
                data = []

                for month in months:
                    if month in self.nonroro_output and vessel_name in self.nonroro_output[month] and \
                            self.nonroro_output[month][vessel_name]:
                        profit = self.nonroro_output[month][vessel_name]['total profit']
                        if 'vessels required' in self.nonroro_output[month][vessel_name]:
                            vessels_required = self.nonroro_output[month][vessel_name]['vessels required']
                            data.append(profit / vessels_required)
                        else:
                            data.append(profit)
                    else:
                        data.append(0.0)

                max_ = max(max_, max(data))

                for i, point in enumerate(data):
                    line_series[vessel_name].append(QPoint(i, point))

            for series in line_series.values():
                self.chart.addSeries(series)
        # Generate Chart For RORO Vessel Overview
        elif type_ == 'RORO':
            self.chart = QtCharts.QChart()
            self.chart.setTheme(QtCharts.QChart.ChartThemeBlueCerulean)

            # RORO DATA
            self.roro_bar_sets = dict()
            for vessel_name in self.roro_vessels:
                self.roro_bar_sets[vessel_name] = BarSet(vessel_name)

            for roro_name, bar_set in self.roro_bar_sets.items():
                data = []

                for month in months:
                    if month in self.roro_output and roro_name in self.roro_output[month] and \
                            self.roro_output[month][roro_name]:
                        profit = self.roro_output[month][roro_name]['total profit']
                        if 'vessels required' in self.roro_output[month][roro_name]:
                            vessels_required = self.roro_output[month][roro_name]['vessels required']
                            data.append(profit / vessels_required)
                        else:
                            data.append(profit)
                    else:
                        data.append(0.0)

                max_ = max(max_, max(data))
                bar_set.append(data)

            bar_series = QtCharts.QBarSeries()
            for bar_set in self.roro_bar_sets.values():
                bar_series.append(bar_set)

            self.chart.addSeries(bar_series)
        # Generate Chart For NONRORO Vessel Overview
        elif type_ == 'NONRORO':
            self.chart = QtCharts.QChart()
            self.chart.setTheme(QtCharts.QChart.ChartThemeBlueCerulean)

            # NONRORO DATA
            line_series = dict()
            for vessel_name in self.nonroro_vessels:
                series = QtCharts.QLineSeries()
                series.setName(vessel_name)
                line_series[vessel_name] = series

            for vessel_name, series in line_series.items():
                data = []

                for month in months:
                    if month in self.nonroro_output and vessel_name in self.nonroro_output[month] and \
                            self.nonroro_output[month][vessel_name]:
                        profit = self.nonroro_output[month][vessel_name]['total profit']
                        if 'vessels required' in self.nonroro_output[month][vessel_name]:
                            vessels_required = self.nonroro_output[month][vessel_name]['vessels required']
                            data.append(profit / vessels_required)
                        else:
                            data.append(profit)
                    else:
                        data.append(0.0)

                max_ = max(max_, max(data))

                for i, point in enumerate(data):
                    line_series[vessel_name].append(QPoint(i, point))

            for series in line_series.values():
                self.chart.addSeries(series)

        self.chart.setTitle('Monthly total profit')
        self.chart.setAnimationOptions(QtCharts.QChart.SeriesAnimations)

        axis_y = QtCharts.QValueAxis()
        axis_y.setRange(0, max_)

        # axis_y.setLabelFormat('%g')
        self.chart.addAxis(axis_y, Qt.AlignLeft)
        if bar_series is not None:
            bar_series.attachAxis(axis_y)

        bar_categories = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        bar_axis_x = QtCharts.QBarCategoryAxis()
        bar_axis_x.append(bar_categories)

        self.chart.addAxis(bar_axis_x, Qt.AlignBottom)
        if bar_series is not None:
            bar_series.attachAxis(bar_axis_x)

        if line_series is not None:
            for series in line_series.values():
                series.attachAxis(bar_axis_x)
                series.attachAxis(axis_y)

        self.chart.legend().setVisible(True)
        self.chart.legend().setAlignment(Qt.AlignBottom)

        self.chart_view.setChart(self.chart)

    def create_month_chart(self, month, type_):
        """
        Genarate Chart For Specific month
        :param month:
        :param type_: RORO / NONRORO
        :return:
        """
        self.chart = QtCharts.QChart()
        self.chart.setTitle('Profit for ' + month)
        self.chart.setTheme(QtCharts.QChart.ChartThemeBlueCerulean)
        self.chart.setAnimationOptions(QtCharts.QChart.SeriesAnimations)

        axis_y = QtCharts.QValueAxis()
        self.chart.addAxis(axis_y, Qt.AlignLeft)

        self.roro_bar_sets = dict()
        self.nonroro_bar_sets = dict()

        if month in self.parent.input_dock_widget.months_list:
            for roro_name in self.roro_vessels:
                try:
                    r_set = BarSet(roro_name)
                    profit = self.roro_output[month][roro_name]['total profit']
                    if 'vessels required' in self.roro_output[month][roro_name]:
                        vessels_required = self.roro_output[month][roro_name]['vessels required']
                        data = profit / vessels_required
                    else:
                        data = profit
                    r_set.append(data)
                    self.roro_bar_sets[roro_name] = r_set
                except KeyError:
                    pass

            for nonroro_name in self.nonroro_vessels:
                try:
                    n_set = BarSet(nonroro_name)
                    profit = self.nonroro_output[month][nonroro_name]['total profit']
                    if 'vessels required' in self.nonroro_output[month][nonroro_name]:
                        vessels_required = self.nonroro_output[month][nonroro_name]['vessels required']
                        data = profit / vessels_required
                    else:
                        data = profit
                    n_set.append(data)
                    self.nonroro_bar_sets[nonroro_name] = n_set
                except KeyError:
                    pass

        bar_series = QtCharts.QBarSeries()
        # Genarate Chart For All types in Specific month
        if type_ == 'All types':
            for bar_set in self.roro_bar_sets.values():
                bar_series.append(bar_set)

            for bar_set in self.nonroro_bar_sets.values():
                bar_series.append(bar_set)
        # Genarate Chart For RORO in Specific month
        elif type_ == 'RORO':
            for bar_set in self.roro_bar_sets.values():
                bar_series.append(bar_set)
        # Genarate Chart For NONRORO in Specific month
        elif type_ == 'NONRORO':
            for bar_set in self.nonroro_bar_sets.values():
                bar_series.append(bar_set)

        self.chart.addSeries(bar_series)
        bar_series.attachAxis(axis_y)

        self.chart.legend().setVisible(True)
        self.chart.legend().setAlignment(Qt.AlignBottom)

        markers = self.chart.legend().markers()
        labels = []

        for marker in markers:
            if marker.label() not in labels and marker.label() in self.roro_vessels:
                labels.append(marker.label())
            else:
                marker.setVisible(False)

        for marker in reversed(markers):
            if marker.label() not in labels and marker.label() in self.nonroro_vessels:
                labels.append(marker.label())
                marker.setVisible(True)

        self.chart_view.setChart(self.chart)

    def connect_legend_markers(self):
        markers = self.chart.legend().markers()

        for marker in markers:
            marker.hovered.connect(self.legend_marker_hovered)

    def _switch_marker(self, marker, alpha):
        brush = marker.labelBrush()
        color = brush.color()
        color.setAlphaF(alpha)
        brush.setColor(color)
        marker.setLabelBrush(brush)

        brush = marker.brush()
        color = brush.color()
        color.setAlphaF(alpha)
        brush.setColor(color)
        marker.setBrush(brush)

        pen = marker.pen()
        color = pen.color()
        color.setAlphaF(alpha)
        pen.setColor(color)
        marker.setPen(pen)

    def _switch_all_markers(self, alpha):
        for marker in self.chart.legend().markers():
            self._switch_marker(marker, alpha)

    def _switch_all_line_series(self, alpha):
        for series in self.chart.series():
            if isinstance(series, QtCharts.QLineSeries):
                self._switch_line_series(series, alpha)

    def _switch_all_bar_sets(self, alpha):
        for series in self.chart.series():
            if isinstance(series, QtCharts.QBarSeries):
                for bar_set in series.barSets():
                    self._switch_bar_set(bar_set, alpha)

            elif isinstance(series, QtCharts.QStackedBarSeries):
                self._switch_line_series(series, alpha)

    def _switch_line_series(self, series, alpha):
        series.setOpacity(alpha)

    def _switch_bar_set(self, bar_set, alpha):
        brush = bar_set.labelBrush()
        color = brush.color()
        color.setAlphaF(alpha)
        brush.setColor(color)
        bar_set.setLabelBrush(brush)

        brush = bar_set.brush()
        color = brush.color()
        color.setAlphaF(alpha)
        brush.setColor(color)
        bar_set.setBrush(brush)

        pen = bar_set.pen()
        color = pen.color()
        color.setAlphaF(alpha)
        pen.setColor(color)
        bar_set.setPen(pen)

    def legend_marker_hovered(self, status):
        marker = self.sender()
        _on = 1.0
        _off = 0.1

        if status:
            self._switch_all_markers(_off)
            self._switch_all_line_series(_off)
            self._switch_all_bar_sets(_off)

            self._switch_marker(marker, _on)

            if isinstance(marker.series(), QtCharts.QLineSeries):
                self._switch_line_series(marker.series(), _on)

            elif isinstance(marker.series(), QtCharts.QBarSeries):
                for bar_set in marker.series().barSets():
                    if bar_set.label() == marker.label():
                        self._switch_bar_set(bar_set, _on)

            elif isinstance(marker.series(), QtCharts.QStackedBarSeries):

                for series in self.chart.series():
                    labels = []
                    for bar_set in series.barSets():
                        labels.append(bar_set.label())

                    if marker.label() in labels:
                        self._switch_line_series(series, _on)
                        # for bar_set in series.barSets():
                        #     if bar_set.label() != marker.label():
                        #         self._switch_bar_set(bar_set, _off)

        else:
            self._switch_all_markers(_on)
            self._switch_all_line_series(_on)
            self._switch_all_bar_sets(_on)

            if isinstance(marker.series(), QtCharts.QStackedBarSeries):

                for series in self.chart.series():
                    self._switch_line_series(series, _on)
                    for bar_set in series.barSets():
                        self._switch_bar_set(bar_set, _on)


class BarSet(QtCharts.QBarSet):

    def __init__(self, label):
        super(BarSet, self).__init__(label)

        self.hovered.connect(self.set_hovered)

    def set_hovered(self, status, index):
        if status:
            # print(self.label(), self.sum())
            pass
