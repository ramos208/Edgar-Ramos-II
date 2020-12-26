import sys
import random
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtCharts import QtCharts


class DateTimeDelegate(QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super(DateTimeDelegate, self).initStyleOption(option, index)
        value = index.data()
        option.text = QDateTime.fromMSecsSinceEpoch(value).toString("dd.MM.yyyy")


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setGeometry(0, 0, 1280, 400)
        self.chart_table()

        self.populate()


    def chart_table(self):
        self.table = QTableWidget(0, 2)
        delegate = DateTimeDelegate(self.table)
        self.table.setItemDelegateForColumn(0, delegate)
        chart = QtCharts.QChart()
        self.chartView = QtCharts.QChartView(chart)
        self.chartView.setFixedSize(600, 430)

        splitter = QSplitter(self)
        splitter.addWidget(self.table)
        splitter.addWidget(self.chartView)
        self.setCentralWidget(splitter)

        series = QtCharts.QLineSeries(name="Odoslané")
        mapper = QtCharts.QVXYModelMapper(self, xColumn=0, yColumn=1)
        mapper.setModel(self.table.model())
        mapper.setSeries(series)
        chart.addSeries(mapper.series())

        self.axis_X = QtCharts.QDateTimeAxis()
        self.axis_X.setFormat("MMM yyyy")
        # self.axis_Y = QtCharts.QAbstractAxis()
        self.axis_Y = QtCharts.QValueAxis()
        # self.axis_Y = QtCharts.QCategoryAxis()

        # axis_y = QtCharts.QBarCategoryAxis()
        # axis_y = [123, 123, 123, 123]

        chart.setAxisX(self.axis_Y, series)
        chart.setAxisY(self.axis_X, series)

        # self.axis_Y.setRange(0, 0)
        import locale
        # locale.setlocale(locale.LC_ALL, 'en_US')

        # self.axis_Y.setLabelFormat('#.##%')

        # print(self.axis_Y.labelFormat())
        # chart.setTitle("Chart")
        curr_locale = QLocale()
        print(curr_locale)
    def test(self):
        print('asdasdasd')
    def addRow(self, dt, value):
        print('a')
        self.table.insertRow(0)
        for col, v in enumerate((dt.toMSecsSinceEpoch(), value)):
            it = QTableWidgetItem()
            it.setData(Qt.DisplayRole, v)
            self.table.setItem(0, col, it)

        if self.table.rowCount() == 1:
            self.axis_X.setRange(dt, dt.addDays(1))
            self.axis_Y.setRange(v, v)

        else:
            t_m, t_M = self.axis_X.min(), self.axis_X.max()
            t_m = min(t_m, dt)
            t_M = max(t_M, dt)

            m, M = self.axis_Y.min(), self.axis_Y.max()
            m = min(m, value)
            M = max(M, value)

            self.axis_X.setRange(t_m, t_M)
            self.axis_Y.setRange(m, M)
            # self.axis_Y.append('slow', 10)
            # self.axis_Y.append('average', 20)
            # self.axis_Y.append('fast', 30)
            # self.axis_Y.append('fast2', 30)
            # self.axis_Y.append('fast3', 40)

    def populate(self):
        for i in range(50):
            # simulate filling table with data as I get them from database.
            value = random.uniform(1, 10000)
            fake_dt_str = QDate.currentDate().addDays(i).toString("dd.MM.yyyy")
            fake_value_str = str(random.uniform(0, 50000))

            # Convert simulated data
            dt = QDateTime.fromString(fake_dt_str, "dd.MM.yyyy")
            value = float(fake_value_str)
            # print(value)
            self.addRow(dt, value)

def main():
    app = QApplication(sys.argv)
    gui = MainWindow()
    gui.show()
    sys.exit(app.exec_())


main()