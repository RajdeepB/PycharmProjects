import time
import calendar
import pandas
import datetime

cal = calendar.month(2017,6)

print(type(cal))
print(cal.split('\n'))

print(calendar.weekday(2017,2,6))

# def get_wom_start(s,m,y):# s is [(x,y)] where x and y is wom; m is moy
#     cal = calendar.month(y, m)
#     mon_list = cal.split('\n')
#     date_start = mon_list[m+2]

s1 = pandas.date_range(2017-6-23, 2017-4-25)

usingDays=pandas.date_range('2017-06-25', end=, freq='D')

print(usingDays)







