import cleaning_module as cl
import csv
from datetime import timedelta

csvFile = open('D:\mhcc_r9.csv')

daydict = {"": "", 1: "Mon", 2: "Tue", 3: "Wed", 4: "Thu", 5: "Fri", 6: "Sat", 7: "Sun"}

csvDReader = csv.DictReader(csvFile)

outputFile = open('output.csv', 'w', newline='')
outputWriter = csv.writer(outputFile)

t_count = 0
count_gen_time_off = 0


for row in csvDReader:
    bid_type = row['.']
    crewid = row['Number']
    avoid = str(cl.get_avoid(row['Pref Type']))
    max_times_roster = cl.setMaxTimesRoster(row['Rqd'])
    region = cl.get_region(row['Rgn'])
    layover = cl.get_transit(row['L/O'])
    transit = cl.get_layover(row['Tod/Port'])
    max_lo_nt = row['Nt']
    bid_points = cl.setPoints((int(row['Wt'])))
    pax = cl.get_pax(row['Px'])
    dow_to_list = cl.get_days_from_dow(row['Remarks'])
    day_range = list(cl.group(dow_to_list))

    if bid_type == 'GEN_TIMEOFF':
        dates_from_wom = get_start_end_date_from_wom(row['Remarks'])
        date_from =
        date_to =
        time_from = 00:00
        time_to = 00:00 + timedelta(hours=row['Durn'])
        for i in range(0, len(day_range)):
            day_from = day_range[i][0]
            day_to = day_range[i][1]
            outputWriter.writerow([bid_type, crewid, date_from, date_to[0], time_from, time_to,  bid_points])

        t_count = t_count + 1
        count_gen_time_off = count_gen_time_off + 1
    else:
        t_count = t_count + 1
        continue

count_translated_bids = count_rule_relax + count_day_off + count_gen_pairing + count_gof

outputFile.close()