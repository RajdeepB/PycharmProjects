import time
import calendar
import xml.etree.cElementTree as ET
import csv
import re



tree1 = ET.parse("D:/export_other_to_crew_bid_MHCC_20170626_080918_latchr.xml")



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
    transits = get_transitData(tree1)
    if t is not None:
        if str(t).strip() in transits:
            return t
    else:
        return ''

def get_layover(l): # checks for transit returns transit
    layovers = get_layoverData(tree1)
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


def get_days(s):  # returns dow in 3 letter day initials eg. 1 - Mon
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

daydict = {"": "", 1: "Mon", 2: "Tue", 3: "Wed", 4: "Thu", 5: "Fri", 6: "Sat", 7: "Sun"}

csvDReader = csv.DictReader(csvFile)

outputFile = open('output.csv', 'w', newline='')
outputWriter = csv.writer(outputFile)
t_count = 0
count_gen_pairing = 0
count_gof = 0
count_day_off = 0
count_rule_relax = 0
count_time_off = 0
count_spec_pairing = 0


for row in csvDReader:
    # print(row)
    bid_type = row['.']
    crewid = row['Number']
    avoid = str(get_avoid(row['Pref Type']))
    max_times_roster = setMaxTimesRoster(row['Rqd'])
    region = get_region(row['Rgn'])
    layover = get_transit(row['L/O'])
    transit = get_layover(row['Tod/Port'])
    max_lo_nt = row['Nt']
    bid_points = setPoints((int(row['Wt'])))
    pax = get_pax(row['Px'])
    dow_to_list = get_days(row['Remarks'])
    # print(type(dow_to_list))
    day_range = list(group(dow_to_list))
    # day_from = int(day_range[0])
    # day_to = day_range[0][1]
    # print(day_range)
    if bid_type == 'GEN_PAIRING' and len(day_range)!=0:
        date_from = conv_d(row['From'])
        date_to = conv_d(row['Until'])
        for i in range(0,len(day_range)):
            day_from = day_range[i][0]
            day_to = day_range[i][1]
            outputWriter.writerow([bid_type, crewid, date_from, date_to, avoid, daydict[day_from], daydict[day_to], max_times_roster, region, layover, max_lo_nt, transit, pax, bid_points])
            t_count= t_count + 1
            count_gen_pairing = count_gen_pairing + 1
    elif bid_type == 'GEN_PAIRING' and len(day_range)==0:
        date_from = conv_d(row['From'])
        date_to = conv_d(row['Until'])
        outputWriter.writerow([bid_type, crewid, date_from, date_to, avoid, daydict[''], daydict[''], max_times_roster, region, layover, max_lo_nt, transit, pax, bid_points])
        t_count = t_count + 1
        count_gen_pairing = count_gen_pairing + 1
    elif bid_type == 'GOLDEN_DO':
        date_from = conv_d(row['From'])
        outputWriter.writerow([bid_type, crewid, date_from, bid_points])
        t_count = t_count + 1
        count_gof = count_gof + 1
    elif bid_type == 'SPEC_DO':
        date_from = conv_d(row['From'])
        date_to = conv_d(row['Until'])
        outputWriter.writerow([bid_type, crewid, date_from, date_to, bid_points])
        t_count = t_count + 1
        count_day_off = count_day_off + 1
    elif bid_type == 'GROUP_DAYS':
        outputWriter.writerow([bid_type, crewid])
        t_count = t_count + 1
        count_rule_relax = count_rule_relax + 1
    elif bid_type == 'WAIVE_WEEK':
        outputWriter.writerow([bid_type, crewid])
        t_count = t_count + 1
        count_rule_relax = count_rule_relax + 1
    elif bid_type == 'SPEC_TIMEOFF':
        t_count = t_count + 1
        count_time_off = count_time_off + 1
    elif bid_type == 'QUAL_TIMEOFF':
        t_count = t_count + 1
        count_time_off = count_time_off + 1
    elif bid_type == 'GEN_TIMEOFF':
        t_count = t_count + 1
        count_time_off = count_time_off + 1
    elif bid_type == 'SPEC_PAIRING':
        t_count = t_count + 1
        count_spec_pairing = count_spec_pairing + 1
    else:
        t_count = t_count + 1
        continue

count_translated_bids = count_rule_relax + count_day_off + count_gen_pairing + count_gof


print("Bids translated : " + str(count_translated_bids) + " out of " + str(t_count)+"\n"
      +"Generic pairing bids : "+ str(count_gen_pairing)+"\n"
      +"Golden day off bis : "+ str(count_gof)+"\n"
      +"Day off bids : "+ str(count_day_off)+"\n"
      +"Rule relaxations : "+ str(count_rule_relax)+"\n")
print("Bids not translated : "+str(count_time_off+ count_spec_pairing)+ " out of " + str(t_count)+"\n"
      +"Specific pairing bids : "+str(count_spec_pairing)+"\n"
      +"Time off bids : "+str(count_time_off))

outputFile.close()




