#import openpyxl
import re
import time
import calendar
import xml.etree.cElementTree as ET
import cProfile
import csv
# import pytest
import unittest


tree1 = ET.parse("D:/export_other_to_crew_bid_MHCC_20170626_080918_latchr.xml")

def get_days(s): # returns dow in 3 letter day initials eg. 1 - Mon
    regex = r"dow:?\D+(\d+)"
    dow = re.findall(regex, s) # returns array but for this case, array will have 1 element only i.e at index 0
    s=dow[0]
    daydict ={"1":"Mon","2":"Tue","3":"Wed","4":"Thu","5":"Fri","6":"Sat","7":"Sun"}
    for i in range (0,len(s)):
        m=s[i:i+1]
        return daydict[m]

def get_dates(s):
    regex = r"wom:?\D+(\d+)"
    matches = re.findall(regex,s)
    s = calendar.monthcalendar(2017,)
    for match in range (0,len(matches)):
        print(str(s[match])+"Jan"+"2017")


def get_dates(s):
    regex = r"wom:?\D+(\d+)"
    matches = re.findall(regex,s)
    s = calendar.monthcalendar(2017,)
    for match in range (0,len(matches)):
        print(str(s[match])+"Jan"+"2017")


def setPoints(n):
    m=n%10
    if n>100:
        return str(100)
    elif n<10:
        return str(10)
    elif (m<5):
        return str((n-m))
    elif (m>=5):
        return str((n+(10-m)))



def setMaxTimesRoster(n):
    if n in ['1', '2', '3', '4', '5', '6', '7']:
        return str(n)
    else:
        try:
            maxTimes=int(n)
            if maxTimes > 7:
                return 'Max'
            elif maxTimes< 1:
                return str(1)
        except ValueError:
            return str(1)


def setMaxTimesRoster2(n):
    if n in ['1', '2', '3', '4', '5', '6', '7']:
        return str(n)
    else:
        return str(1)

def convert_dt_gen(d):
    if d is not None:
        final = time.strptime(d, "%d-%b-%y")
        final2 = time.strftime("%d/%m/%y",final)
        return str(final2)
    else:
        return None

def convert_dt_off(d):
    if d is not None:
        final = time.strptime(d, "%d%b%y %H%M")
        final2 = time.strftime("%d/%m/%y",final)
        return str(final2)
    else:
        return None

def convert_dt_offy(d):
    if d is not None:
        final = time.strptime(d, "%d%b%Y %H%M")
        final2 = time.strftime("%d/%m/%y",final)
        return str(final2)
    else:
        return None


def conv_d(d):
    if d is not None:
        try:
            final = time.strptime(d, "%d%b%Y %H%M")
        except TypeError:
            final = time.strptime(d, "%d%b%y %H%M")
        except TypeError:
            final = time.strptime(d, "%d-%b-%y")
        finally:
            return time.strftime("%d/%m/%y",final)
    else:
        return None

def conv_t(d):
    if d is not None:
        try:
            final = time.strptime(d, "%d%b%Y %H%M")
        except TypeError:
            final = time.strptime(d, "%d%b%y %H%M")
        finally:
            return time.strftime("%H:%M",final)
    else:
        return None



def get_avoid(d):
    av = str(d)
    if av in ['AGT', 'AST', 'ATDA']:
        return True
    else:
        return ''


def get_layoverData(tree):
    layovers=[]
    for node in tree.iterfind(".//destinationdata/destinations"):
        destinationData = node.findall('destination')
        for node2 in destinationData:
            if node2.attrib['layover']=="true":
                layovers.append(node2.attrib['airport'])
    return layovers


def get_transitData(tree):
    transits=[]
    for node in tree.iterfind(".//destinationdata/destinations"):
        destinationData = node.findall('destination')
        for node2 in destinationData:
            if node2.attrib['stop']=="true":
                transits.append(node2.attrib['airport'])
    return transits


def get_transit(t):
    transits = get_transitData(tree1)
    if t is not None:
        if str(t) in transits:
            return t
    else:
        return ''



# class simpleTest(unittest.TestCase):
#     def testConvertDate(self):
#         self.assertEquals(convert_dt_gen('24-Dec-16'),'24/12/16')




# print(convert_dt_gen('26-Mar-17'))
#
# print(convert_dt_off('19DEC16 1915'))
#
# print(convert_dt_offy('19DEC2016 1915'))

# print(conv_t('19DEC2016 1915'))

# print(get_layoverData(tree1))

print(get_avoid('GTOD'))


# csvFile = open('D:\Book1_mhcc_r2.csv')
#
# print(type(csvFile)) # class '_io.TextIOWrapper'
# csvReader = csv.reader(csvFile) #returns an 'reader' iterator ; csvFile needs to be of iterable type, or anything that supports the iterator protocol
# print(type(csvReader)) # class '_csv.reader' the reader object reads sequences
# print(csv.field_size_limit)
#
# csvDReader = csv.DictReader(csvFile)
#
# print(csvDReader.fieldnames)
#
# for row in csvDReader:
#     bid_type = row['.']
#     num = row['Number']
#     avoid = str(get_avoid(row['Pref Type']))
#     max_times_roster = setMaxTimesRoster(row['Rqd'])
#     bid_points = setPoints((int(row['Wt'])))
#     layover = row['Tod/Port']
#     region = row['Rgn']
#     try:
#         if bid_type in ('SPEC_PAIRING','SPEC_TIMEOFF'):
#             date_from = convert_date2(row['From'])
#             date_to = convert_date2(row['Until'])
#         elif bid_type in ('GEN_PAIRING','SPEC_DO','GEN_TIMEOFF'):
#             date_from = convert_date(row['From'])
#             date_to = convert_date(row['Until'])
#         elif bid_type in ('GOLDEN_DO'):
#             date_from = convert_date(row['From'])
#             date_to =''
#         else:
#             date_from = ''
#             date_to = ''
#     except ValueError:
#         print('value error')
#     bid_object = [num, avoid, date_from, date_to, max_times_roster, bid_points, layover, region]
#     print(','.join(bid_object))
#

# get_days("dow:257, wom:1234")

# print(calendar.monthrange(2017,2))
#
# print(type('hello'))

# get_dates("dow:257, wom:23")
# cProfile.run('get_days("dow:257, wom:1234")')


# print(time.asctime(time.localtime(time.time())))
#
# print(time.localtime())

# print(time.localtime(time.time()))
#
# print(calendar.month(2017,1))
#
# print(time.clock())
#
# print(time.altzone(1))

# print(calendar.calendar(2017,2,1,6))

# s=calendar.monthcalendar(2017,2)

# print (s[1])
#
#
#
# w1= re.findall(r"[a-zA-Z]{3}","")
# print(w1)

# cutoff future date using this is somewhere in 2038
# get_dates("dow:67, wom:1234")

# s="dow:67, wom:.......1234"
# regex = r"wom:?\D+(\d+)"
# matches = re.findall(regex, s)
# for match in matches:
#     print(match)