import sys

from PySide2.QtCharts import QtCharts
from PySide2.QtCore import QPoint
from PySide2.QtGui import QColor, QPen, QFont, QBrush, QLinearGradient, Qt, QGradient
from PySide2.QtWidgets import QMainWindow, QApplication


class MyChart(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Chart Formatting Demo')
        self.resize(1200, 800)

        self.initChart()

        self.setCentralWidget(self.chartView)

    def initChart(self):
        series = QtCharts.QLineSeries()

        data = [
            QPoint(0, 6),
            QPoint(9, 4),
            QPoint(15, 20),
            QPoint(18, 12),
            QPoint(28, 25)
        ]

        series.append(data)

        # creating chart object
        chart = QtCharts.QChart()
        chart.legend().hide()
        chart.addSeries(series)

        pen = QPen(QColor(200, 200, 200))
        pen.setWidth(5)
        series.setPen(pen)

        font = QFont('Open Sans')
        font.setPixelSize(40)
        font.setBold(True)
        chart.setTitleFont(font)
        chart.setTitleBrush(QBrush(Qt.yellow))
        chart.setTitle('Custom Chart Demo')

        backgroundGradient = QLinearGradient()
        backgroundGradient.setStart(QPoint(0, 0))
        backgroundGradient.setFinalStop(QPoint(0, 1))
        backgroundGradient.setColorAt(0.0, QColor(175, 201, 182))
        backgroundGradient.setColorAt(1.0, QColor(51, 105, 66))
        backgroundGradient.setCoordinateMode(QGradient.ObjectBoundingMode)
        chart.setBackgroundBrush(backgroundGradient)

        plotAreaGraident = QLinearGradient()
        plotAreaGraident.setStart(QPoint(0, 1))
        plotAreaGraident.setFinalStop(QPoint(1, 0))
        plotAreaGraident.setColorAt(0.0, QColor(222, 222, 222))
        plotAreaGraident.setColorAt(1.0, QColor(51, 105, 66))
        plotAreaGraident.setCoordinateMode(QGradient.ObjectBoundingMode)
        chart.setPlotAreaBackgroundBrush(plotAreaGraident)
        chart.setPlotAreaBackgroundVisible(True)

        # customize axis
        axisX = QtCharts.QCategoryAxis()
        axisY = QtCharts.QCategoryAxis(labelsPosition=QtCharts.QCategoryAxis.AxisLabelsPositionOnValue, startValue=0.0)

        labelFont = QFont('Open Sans')
        labelFont.setPixelSize(25)

        axisX.setLabelsFont(labelFont)
        axisY.setLabelsFont(labelFont)

        axisPen = QPen(Qt.white)
        axisPen.setWidth(2)

        axisX.setLinePen(axisPen)
        axisY.setLinePen(axisPen)

        axixBrush = QBrush(Qt.white)
        axisX.setLabelsBrush(axixBrush)
        axisY.setLabelsBrush(axixBrush)

        axisX.setRange(0, 40)
        axisX.append('low', 10)
        axisX.append('medium', 20)
        axisX.append('high', 30)
        axisX.append('high2', 40)

        axisY.setRange(0, 30)
        axisY.append('123', 0)
        axisY.append('123,123', 10)
        axisY.append('234,234', 20)
        axisY.append('234,234.1', 30)


        axisX.setGridLineVisible(False)
        axisY.setGridLineVisible(False)

        chart.addAxis(axisX, Qt.AlignBottom)
        chart.addAxis(axisY, Qt.AlignLeft)

        series.attachAxis(axisX)
        series.attachAxis(axisY)

        self.chartView = QtCharts.QChartView(chart)
        self.chartView.setFixedSize(600, 430)
        # self.chartView.setRenderHint(QPainter.Antialiasing)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    chartDemo = MyChart()
    chartDemo.show()

    sys.exit(app.exec_())