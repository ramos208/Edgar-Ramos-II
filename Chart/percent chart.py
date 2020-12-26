import xlsxwriter

workbook = xlsxwriter.Workbook('chart.xlsx')
worksheet = workbook.add_worksheet()

worksheet.write_column('A1', [10, 40, 50])

chart = workbook.add_chart({'type': 'bar', 'subtype': 'column'})

chart.add_series({'values': '=Sheet1!$A$1', 'data_labels': {'value': 1}})
chart.add_series({'values': '=Sheet1!$A$2', 'data_labels': {'value': 1}})
chart.add_series({'values': '=Sheet1!$A$3', 'data_labels': {'value': 1}})

chart.set_legend({'none': True})
# chart.set_x_axis({'label_position': 'none'})

worksheet.insert_chart('D2', chart)

workbook.close()