import time
import calendar
import xml.etree.cElementTree as ET
import re
import datetime
from datetime import timedelta

source_xml = ET.parse("D:/export_other_to_crew_bid_MHCC_20170626_080918_latchr.xml")


def get_dates(s):
    regex = r"wom:?\D+(\d+)"
    matches = re.findall(regex,s)
    s = calendar.monthcalendar(2017,)
    for match in range (0,len(matches)):
        print(str(s[match])+"Jan"+"2017")


def setPoints(n): # returns bid points as a string
    m=n%10
    if n>100:
        return str(100)
    elif n<10:
        return str(10)
    elif (m<5):
        return str((n-m))
    elif (m>=5):
        return str((n+(10-m)))


def setMaxTimesRoster(n): # returns max times roster as string
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


def conv_d(d):# returns date in a dd/mm/yy format
   if d is not None:
        length = len((str(d).strip()))
        if length>=8 and length <=9:
            final_d = time.strptime(d, "%d-%b-%y")
        elif length>=10 and length <=12:
            final_d = time.strptime(d, "%d%b%y %H%M")
        elif length>=13 and length <=14:
            final_d = time.strptime(d, "%d%b%Y %H%M")
        return time.strftime("%d/%m/%y",final_d)
   else:
        return ''

def conv_t(d): # returns time in an hh:mm
    if d is not None:
        try:
            final_t = time.strptime(d, "%d%b%Y %H%M")
        except TypeError:
            final_t = time.strptime(d, "%d%b%y %H%M")
        finally:
            return time.strftime("%H:%M",final_t)
    else:
        return ''


def get_avoid(d): # returns boolean
    av = str(d)
    if av in ['AGT', 'AST', 'ATDA']:
        return True
    else:
        return ''

def get_region(r): # returns region
    regions ={
        'AUS':'AUSTRALIA',
        'NAM':'AMERICA',
        'ORI':'ASIA',
        'NZ':'NEW ZEALAND',
        'PAC':'PACIFIC',
        'SAM':'AMERICA'}
    if r is not None:
        return regions.get(r)
    else:
        return ''

def get_layoverData(tree): # returns layover ports present in the JCR JCB export file in a list
    layovers=[]
    for node in tree.iterfind(".//destinationdata/destinations"):
        destinationData = node.findall('destination')
        for node2 in destinationData:
            if node2.attrib['layover']=="true":
                layovers.append(node2.attrib['airport'])
    return layovers


def get_transitData(tree): # returns transit ports present in the JCR JCB export file in a list
    transits=[]
    for node in tree.iterfind(".//destinationdata/destinations"):
        destinationData = node.findall('destination')
        for node2 in destinationData:
            if node2.attrib['stop']=="true":
                transits.append(node2.attrib['airport'])
    return transits


def get_transit(t): # checks for transit returns transit
    transits = get_transitData(source_xml)
    if t is not None:
        if str(t).strip() in transits:
            return t
    else:
        return ''

def get_layover(l): # checks for transit returns transit
    layovers = get_layoverData(source_xml)
    if l is not None:
        if str(l).strip() in layovers:
            return l
    else:
        return ''


def get_pax(s):
    px = str(s).strip()
    if px == "ON":
        return "PAX to home base"
    else:
        return ''


def group(L):
    if len(L) == 0:
        return (0,0)
    else:
        first = last = L[0]
        for n in L[1:]:
            if (n - 1) == last:  # Part of the group, bump the end
                last = n
            else:  # Not part of the group, yield current group and start a new
                yield first, last
                first = last = n
        yield first, last  # Yield the last group


def get_days_from_dow(s):  # returns dow in 3 letter day initials eg. 1 - Mon
    s_stripped = "".join(s.split())
    if 'dow' in s_stripped:
        # print("I'm in")
        regex = r"dow:?\D+(\d+)"
        dow = re.findall(regex, s_stripped)  # returns array but for this case, array will have 1 element only i.e at index 0
        dow_list = []
        for i in dow[0]:
            dow_list.append(int(i))
        return dow_list
    else:
        return []



def get_end_date_time_from_duration(start, durn):
    duration = int(durn)
    stripped_time = time.strptime(start, '%d%b%Y %H%M') #returns tuple
    start_date = datetime.datetime(stripped_time.tm_year,stripped_time.tm_mon,stripped_time.tm_mday, stripped_time.tm_hour, stripped_time.tm_min, stripped_time.tm_sec)

    end_date_time = start_date + timedelta(hours=duration)

    end_date_time_stripped = time.strptime(str(end_date_time),'%Y-%m-%d %H:%M:%S')

    end_date = time.strftime('%d/%m/%y', end_date_time_stripped)
    end_time = time.strftime('%H:%M',end_date_time_stripped)
    return [end_date, end_time]


def get_start_end_date_from_wom(start, x, y):
    stripped_time = time.strptime(start, '%d%b%Y %H%M')  # returns tuple
    start_date = datetime.datetime(stripped_time.tm_year,
                                   stripped_time.tm_mon,
                                   stripped_time.tm_mday,
                                   stripped_time.tm_hour,
                                   stripped_time.tm_min,
                                   stripped_time.tm_sec)

    start_date_time = start_date + timedelta(days=x-1)*7
    end_date_time = start_date + timedelta(days=y)*7 - timedelta(days=1)

    start_date_time_stripped = time.strptime(str(start_date_time), '%Y-%m-%d %H:%M:%S')
    end_date_time_stripped = time.strptime(str(end_date_time), '%Y-%m-%d %H:%M:%S')

    start_date = time.strftime('%d/%m/%y', start_date_time_stripped)
    end_date = time.strftime('%d/%m/%y', end_date_time_stripped)

    return [start_date, end_date]