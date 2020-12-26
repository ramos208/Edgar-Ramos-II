# import pymongo
# from PySide2.QtWidgets import QDesktopWidget, QApplication
#
# a = [1,2,4]
# b = [1,2,3]
#
# print(a[1:])
# print(' '.join([str(elem) for elem in a]))
#
# c =all(item in b for item in a)
# print(c)
# for d in a:
#     if d in b:
#         pass
#     else:
#         print(d)
#
# app = QApplication([])
# screen_resolution = app.desktop().screenGeometry()
# width, height = screen_resolution.width(), screen_resolution.height()
#
# print(width * 0.013 + height * 0.013)
#
#
# from sys import platform
# print(platform)
# # if platform == "linux" or platform == "linux2":
# #     # linux
# # elif platform == "darwin":
# #     # OS X
# # elif platform == "win32":
# #     # Windows...
#
# d_ = '   (   123   ,  1232 )   ,   ( 123 , 123 )    '
#
# print("".join(d_.split()))
#
# a = [1,2]
# data = dict()
# data['region name'] ={'$in': a}
#
# print(data)
#
# dict_1 = {'REGION LABEL': 'MROV1', 'NAME OF PORT': '12', 'LONGITUDE': '12', 'LATITUDE': '12'}
# dict_2 = {'REGION LABEL': 'MROV', 'NAME OF PORT': '12', 'LONGITUDE': '12', 'LATITUDE': '12'}
# unmatched_item = set(dict_1.items()) ^ set(dict_2.items())
# print(len(unmatched_item))


# roro = {'JANUARY': {'STARLITE JUPITER': 402737.02, 'STARLITE SATURN': 546571.67, 'SHIP 1': 150814.05, 'SHIP 2': 225740.13, 'BALENO 1': ''}, 'FEBRUARY': {'STARLITE JUPITER': 287669.3, 'STARLITE SATURN': 402737.02, 'SHIP 1': 120651.24, 'SHIP 2': 180592.1, 'BALENO 1': ''}, 'MARCH': {'STARLITE JUPITER': 316436.23, 'STARLITE SATURN': 431503.95, 'SHIP 1': 120651.24, 'SHIP 2': 180592.1, 'BALENO 1': ''}, 'APRIL': {'STARLITE JUPITER': 575338.6, 'STARLITE SATURN': 747940.18, 'SHIP 1': 211139.68, 'SHIP 2': 316036.18, 'BALENO 1': ''}, 'MAY': {'STARLITE JUPITER': 604105.53, 'STARLITE SATURN': 805474.04, 'SHIP 1': 211139.68, 'SHIP 2': 316036.18, 'BALENO 1': ''}, 'JUNE': {'STARLITE JUPITER': 489037.81, 'STARLITE SATURN': 632872.46, 'SHIP 1': 180976.87, 'SHIP 2': 270888.15, 'BALENO 1': ''}, 'JULY': {'STARLITE JUPITER': 402737.02, 'STARLITE SATURN': 517804.74, 'SHIP 1': 150814.05, 'SHIP 2': 225740.13, 'BALENO 1': ''}, 'AUGUST': {'STARLITE JUPITER': 373970.09, 'STARLITE SATURN': 489037.81, 'SHIP 1': 150814.05, 'SHIP 2': 225740.13, 'BALENO 1': ''}, 'SEPTEMBER': {'STARLITE JUPITER': 402737.02, 'STARLITE SATURN': 546571.67, 'SHIP 1': 150814.05, 'SHIP 2': 225740.13, 'BALENO 1': ''}, 'OCTOBER': {'STARLITE JUPITER': 402737.02, 'STARLITE SATURN': 517804.74, 'SHIP 1': 150814.05, 'SHIP 2': 225740.13, 'BALENO 1': ''}, 'NOVEMBER': {'STARLITE JUPITER': 431503.95, 'STARLITE SATURN': 546571.67, 'SHIP 1': 150814.05, 'SHIP 2': 225740.13, 'BALENO 1': ''}, 'DECEMBER': {'STARLITE JUPITER': 373970.09, 'STARLITE SATURN': 489037.81, 'SHIP 1': 150814.05, 'SHIP 2': 225740.13, 'BALENO 1': ''}}
# month = []
# # for d in roro:
#     # month.append(d)
#
# vessel_roro = []
# for k,i in roro['JANUARY'].items():
#     vessel_roro.append(k)
#
# print(vessel_roro)
# roro_sum = dict()
# first = True
# for i in roro.values():
#     if first:
#         for d in vessel_roro:
#             print(i[d])
#             if i[d] == '':
#                 roro_sum[d] = 0
#             else:
#                 roro_sum[d] =float(i[d])
#         first = False
#     else:
#         for d in vessel_roro:
#             if i[d] == '':
#                 roro_sum[d] += 0
#             else:
#                 roro_sum[d] += float(i[d])
# print(roro_sum)

# print(round(123123.5))
# print("{:,}".format(round(123123.5)))

import numpy
a = 2.71828
# b = 22300
b = 600
c = b / 3
print(c)

print(numpy.power(a,b))
# print(a**b)


