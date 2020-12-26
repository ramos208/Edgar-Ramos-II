import xlsxwriter
roro = {'FAST CAT M11': [0.0, 411105.3022582353, 448687.7805124264, 654588.4175513051, 632665.3052363603, 516090.0254664155, 437204.24549031246, 460519.3014443014, 429548.5554755699, 457387.4282564522, 523397.7295713971, 511218.222729761], 'LITE FERRY 88': [0.0, 347920.36345529405, 380485.2047089705, 554746.912744522, 535750.7553465441, 434739.44219856616, 370534.836548125, 390737.0991777205, 363901.2577742279, 388023.36240658094, 441071.4946645588, 430518.0738879043]}
# roro = {}
nonroro = {'OCEAN JET 1': [0.0, 616582.8971428571, 884454.8281967214, 1154599.0615384616, 1260781.2564705885, 676462.9557446808, 609942.3655813953, 639129.8666666667, 609797.1828571428, 814596.857142857, 699518.2748936169, 1098608.2799999998], 'OCEAN JET 2': [0.0, 746389.8228571429, 1113757.9318032786, 1418507.4184615384, 1559387.343529412, 837525.5642553191, 770453.5144186047, 798912.3333333335, 738175.537142857, 1010100.1028571429, 866070.2451063828, 1398228.72]}
# nonroro = {}
vessel_header = list(roro.keys()) + list(nonroro.keys())
vessel_data = list(roro.values()) + list(nonroro.values())

workbook = xlsxwriter.Workbook('chart_test.xlsx')
worksheet = workbook.add_worksheet()
bold = workbook.add_format({'bold': 1})

worksheet.write(0,0,'Months',bold)
header = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
for row in range(0,len(header)):
    worksheet.write(row + 1,0,header[row])

for col in range(0,len(vessel_header)):
    worksheet.write(0,col + 1,vessel_header[col])

col = 0
for data in vessel_data:
    col += 1
    for row in range(0, len(data)):
        worksheet.write(row + 1, col, round(data[row]))

# roro
chart_bar = workbook.add_chart({'type': 'column'})
# nonroro
chart_line = workbook.add_chart({'type': 'line'})

if len(roro) != 0:
    for legend in range(0, len(roro.keys())):
        chart_bar.add_series({
            'name': ['Sheet1', 0, legend + 1],
            'categories': ['Sheet1', 1, 0, 12, 0],
            'values': ['Sheet1', 1, legend + 1, 12, legend + 1],
            'data_labels': {'value': True, 'position': 'end'}

        })

    if len(nonroro) != 0:
        for legend in range(len(roro.keys()), len(vessel_header)):
            chart_line.add_series({
                'name': ['Sheet1', 0, legend + 1],
                'categories': ['Sheet1', 1, 0, 12, 0],
                'values': ['Sheet1', 1, legend + 1, 12, legend + 1],
                'labels': {'value': True, 'position': 'end'}
            })

    chart_bar.combine(chart_line)
    worksheet.insert_chart('A14', chart_bar, {'x_offset': 25, 'y_offset': 10})
else:
    for legend in range(0, len(vessel_header)):
        chart_line.add_series({
            'name': ['Sheet1', 0, legend + 1],
            'categories': ['Sheet1', 1, 0, 12, 0],
            'values': ['Sheet1', 1, legend + 1, 12, legend + 1],
        })
    worksheet.insert_chart('A14', chart_line, {'x_offset': 25, 'y_offset': 10})



# Add a chart title and some axis labels.
chart_bar.set_title ({'name': 'Monthly total profit'})
chart_bar.set_x_axis({'label_position': 'none'})
chart_line.set_x_axis({'label_position': 'none'})

# Set an Excel chart style.
chart_bar.set_style(10)
workbook.close()