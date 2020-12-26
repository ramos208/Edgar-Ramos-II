import xlsxwriter
from PySide2.QtWidgets import *
from PySide2.QtGui import *
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PushButton")
        # self.setGeometry(300,300,300,400)

        # self.setGeometry(300,300,300,400)

        self.setMinimumHeight(500)
        self.setMinimumWidth(300)
        self.setMaximumHeight(500)
        self.setMaximumWidth(300)

        self.setIcon()
        self.setButton()

        self.roro = {'ROMBLON': {'FEBRUARY': {
            'BALENO 1': {'total revenue': 41278800.0, 'total cost': 1467113.43, 'total profit': 39811686.57,
                         'profit per trip': 780621.3052941177, 'vessels required': 1, 'trips per month': 51,
                         'travel time': 1.7748333333333333, 'pax util': 1.0, 'cargo util': 0.9938013915243517}},
            'MARCH': {'BALENO 1': {'total revenue': 45084750.0, 'total cost': 1610948.08,
                                   'total profit': 43473801.92, 'profit per trip': 776317.8914285714,
                                   'vessels required': 1, 'trips per month': 56,
                                   'travel time': 1.7748333333333333, 'pax util': 0.9828443877551021,
                                   'cargo util': 0.9896313364055299}}, 'APRIL': {
                'BALENO 1': {'total revenue': 80852800.0, 'total cost': 2876693.0, 'total profit': 77976107.0,
                             'profit per trip': 779761.07, 'vessels required': 1, 'trips per month': 100,
                             'travel time': 1.7748333333333333, 'pax util': 1.0, 'cargo util': 0.9926451612903225}},
            'MAY': {'BALENO 1': {'total revenue': 87362400.0, 'total cost': 3106828.44,
                                 'total profit': 84255571.56, 'profit per trip': 780144.1811111112,
                                 'vessels required': 1, 'trips per month': 108,
                                 'travel time': 1.7748333333333333, 'pax util': 1.0,
                                 'cargo util': 0.9931600955794504}}, 'JUNE': {
                'BALENO 1': {'total revenue': 68216450.0, 'total cost': 2445189.05, 'total profit': 65771260.95,
                             'profit per trip': 773779.5405882354, 'vessels required': 1, 'trips per month': 85,
                             'travel time': 1.7748333333333333, 'pax util': 0.8936554621848739,
                             'cargo util': 0.9946110056925996}}}, 'BALATERO': {'FEBRUARY': {
            'FAST CAT M-1': {'total revenue': 52288020.0, 'total cost': 1898617.3800000001, 'total profit': 50389402.62,
                             'profit per trip': 763475.7972727272, 'vessels required': 1, 'trips per month': 66,
                             'travel time': 0.335625, 'pax util': 0.5971349862258953,
                             'cargo util': 0.9862532610876982}}, 'MARCH': {
            'FAST CAT M-1': {'total revenue': 52886500.0, 'total cost': 1841083.52, 'total profit': 51045416.48,
                             'profit per trip': 797584.6325, 'vessels required': 1, 'trips per month': 64,
                             'travel time': 0.335625, 'pax util': 1.0, 'cargo util': 0.9888762417218543}}, 'APRIL': {
            'FAST CAT M-1': {'total revenue': 83024210.0, 'total cost': 2876693.0, 'total profit': 80147517.0,
                             'profit per trip': 801475.17, 'vessels required': 1, 'trips per month': 100,
                             'travel time': 0.335625, 'pax util': 0.9836, 'cargo util': 0.9957615894039735}}, 'MAY': {
            'FAST CAT M-1': {'total revenue': 82395250.0, 'total cost': 2847926.07, 'total profit': 79547323.93,
                             'profit per trip': 803508.3225252526, 'vessels required': 1, 'trips per month': 99,
                             'travel time': 0.335625, 'pax util': 1.0, 'cargo util': 0.9967221887751689}}, 'JUNE': {
            'FAST CAT M-1': {'total revenue': 67739500.0, 'total cost': 2358888.2600000002, 'total profit': 65380611.74,
                             'profit per trip': 797324.5334146342, 'vessels required': 1, 'trips per month': 82,
                             'travel time': 0.335625, 'pax util': 1.0, 'cargo util': 0.988531739622032}}}}


        self.nonroro ={'ROMBLON': {'FEBRUARY':
                                       {'BLUE PENGUIN 2': {'total revenue': 61040.00000000001, 'total cost': 37153.68,
                                                     'total profit': 23886.320000000007,
                                                     'profit per trip': 11943.160000000003, 'trips per month': 2.0,
                                                     'travel time': 2.1298, 'pax util': 0.6411764705882353,
                                                     'cargo util': 0}}, 'MARCH': {'BLUE PENGUIN 2': {}}, 'APRIL': {
            'BLUE PENGUIN 2': {'total revenue': 1406720.0, 'total cost': 557305.2, 'total profit': 849414.8,
                               'profit per trip': 28313.826666666668, 'trips per month': 30.0, 'travel time': 2.1298,
                               'pax util': 0.9850980392156863, 'cargo util': 0}}, 'MAY': {
            'BLUE PENGUIN 2': {'total revenue': 2430400.0, 'total cost': 965995.68, 'total profit': 1464404.3199999998,
                               'profit per trip': 28161.621538461535, 'trips per month': 52.0, 'travel time': 2.1298,
                               'pax util': 0.9819004524886877, 'cargo util': 0}}, 'JUNE': {'BLUE PENGUIN 2': {}}},
         'BALATERO': {'FEBRUARY': {'BLUE PENGUIN 2': {}, 'OCEAN JET 1': {}}, 'MARCH': {
             'BLUE PENGUIN 2': {'total revenue': 126195.34883720931, 'total cost': 55730.520000000004,
                                'total profit': 70464.82883720931, 'profit per trip': 23488.27627906977,
                                'trips per month': 3.0, 'travel time': 0.3222, 'pax util': 0.8837209302325582,
                                'cargo util': 0},
             'OCEAN JET 1': {'total revenue': 92790.6976744186, 'total cost': 37153.68,
                             'total profit': 55637.017674418596, 'profit per trip': 27818.508837209298,
                             'trips per month': 2.0, 'travel time': 0.537, 'pax util': 0.8837209302325582,
                             'cargo util': 0}}, 'APRIL': {'BLUE PENGUIN 2': {}, 'OCEAN JET 1': {}}, 'MAY': {
             'BLUE PENGUIN 2': {'total revenue': 2250891.8725936296, 'total cost': 891688.3200000001,
                                'total profit': 1359203.5525936296, 'profit per trip': 28316.74067903395,
                                'trips per month': 48.0, 'travel time': 0.3222, 'pax util': 0.9851592579628982,
                                'cargo util': 0},
             'OCEAN JET 1': {'total revenue': 1810230.1365068252, 'total cost': 650189.4,
                             'total profit': 1160040.7365068253, 'profit per trip': 33144.021043052155,
                             'trips per month': 35.0, 'travel time': 0.537, 'pax util': 0.985159257962898,
                             'cargo util': 0}}, 'JUNE': {
             'BLUE PENGUIN 2': {'total revenue': 484850.39755351684, 'total cost': 204345.24,
                                'total profit': 280505.15755351685, 'profit per trip': 25500.46886850153,
                                'trips per month': 11.0, 'travel time': 0.3222, 'pax util': 0.9259938837920489,
                                'cargo util': 0},
             'OCEAN JET 1': {'total revenue': 388917.43119266053, 'total cost': 148614.72,
                             'total profit': 240302.71119266053, 'profit per trip': 30037.838899082566,
                             'trips per month': 8.0, 'travel time': 0.537, 'pax util': 0.9259938837920489,
                             'cargo util': 0}}}}

        self.test()
    def test(self):
        months = ['FEBRUARY', 'MARCH', 'APRIL', 'MAY', 'JUNE']
        route = ['ROMBLON','BALATERO']
        for r in route:
            for m in months:
                print(r,m,self.roro[r][m])
                        # print(m,d)

        # workbook = xlsxwriter.Workbook('test.xlsx')
        #
        # worksheet = workbook.add_worksheet("cba")
        #
        # col_headers = 0
        # cell_format_header = workbook.add_format(
        #     {
        #         'bg_color': '#18476f',
        #         'font_color': 'white',
        #         'bold': True,
        #     })
        #
        # cell_format_num = workbook.add_format(
        #     {
        #         'bold': True,
        #         'num_format': '#,##0.00'
        #     })
        #
        # cell_format_currency = workbook.add_format(
        #     {
        #         'bold': True,
        #         'num_format': '#,##0.00'
        #     })
        #
        # # 'num_format': '$#,##0.00'
        #
        # # header
        # headers_cost_benefit_analysis = ['Time frame', 'Vessel type', 'Vessel name', 'Trips per month',
        #                                  'Passenger utilization ratio',
        #                                  'Cargo utilization ratio', 'Travel time (h)', 'Vessels required',
        #                                  'Profit per trip (PHP)',
        #                                  'Total revenue (PHP)', 'Total Cost (PHP)', 'Total profit (PHP)']
        # header = headers_cost_benefit_analysis
        # for col in range(0, len(header)):
        #     worksheet.write(0, col, header[col], cell_format_header)

        # cba
        # last_row = 0
        # for row in range(self.table.rowCount()):
        #     for column in range(self.table.columnCount()):
        #         if self.table.item(row, column):
        #             worksheet.write(row + 2, column, self.table.item(row, column).text())
        #             last_row = row + 3
        #
        # worksheet.write(last_row, 0, '')
        # worksheet.write(last_row + 1, 0, '')
        # worksheet.write(last_row + 2, 0, '')

        # headers = ['Month', 'Remaining passengers', 'Remaining cargo']
        # for col in range(0, len(headers)):
        #     worksheet.write(last_row + 3, col, headers[col], cell_format_header)

        # row = last_row + 5
        # time_frame = self.parent.input_dock_widget.months_list
        # for index, value in enumerate(time_frame):
        #     row_ = row + index
        #     worksheet.write(row_, 0, time_frame[index])
        #     worksheet.write(row_, 1, self.engine.remaining_passenger_list[index], cell_format_num)
        #     worksheet.write(row_, 2, self.engine.remaining_cargo_list[index], cell_format_num)
        #     worksheet.write(row_ + 2, 0, '')

        # col_width = []
        # for i in range(self.table.columnCount()):
        #     col_width.append(self.table.columnWidth(i) / 6)
        #
        # for i in range(0, len(col_width)):
        #     if i == 1:
        #         worksheet.set_column(i, i, col_width[i] + 10)
        #     elif i == 2:
        #         worksheet.set_column(i, i, col_width[i] + 15)
        #     else:
        #         worksheet.set_column(i, i, col_width[i])
            # if i in range(1,2):
            #     if i == 1:
            #         worksheet.set_column(i,i, col_width[i]+10)
            #     if i == 2:
            #         worksheet.set_column(i, i, col_width[i] + 15)
            # else:
            #     worksheet.set_column(i,i, col_width[i])
        # workbook.close()


    def setIcon(self):
        appIcon = QIcon("icon/icon.png")
        self.setWindowIcon(appIcon)

    def setButton(self):
        btnLogin = QPushButton("Login", self)
        btnLogin.move(50,200)

        lbl = QTextEdit("Login", self)
        lbl.selectAll()

        btnLogin.clicked.connect(self.export_btn_clicked)

    def export_btn_clicked(self):
        file_name, _ = QFileDialog.getSaveFileName(self, caption="Export cost benefit analysis report", filter="xlsx(*.xlsx)")

        if file_name:
            self.export_table(file_name)

            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setText("Export success!")
            msg_box.setInformativeText("Cost benefit analysis report has been exported successfully.")
            msg_box.exec_()




myApp = QApplication(sys.argv)
window = Window()
window.show()

# time.sleep(5)
window.resize(300,500)

myApp.exec_()
sys.exit(0)