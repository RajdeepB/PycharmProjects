import cleaning_module as cl
import csv


csvFile = open('D:\mhcc_r9.csv')

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
count_spec_time_off = 0
count_gen_time_off = 0
count_qual_time_off = 0

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
    if bid_type == 'GEN_PAIRING' and len(day_range)!=0:
        date_from = cl.conv_d(row['From'])
        date_to = cl.conv_d(row['Until'])
        for i in range(0,len(day_range)):
            day_from = day_range[i][0]
            day_to = day_range[i][1]
            outputWriter.writerow([bid_type, crewid, date_from, date_to, avoid, daydict[day_from], daydict[day_to], max_times_roster, region, layover, max_lo_nt, transit, pax, bid_points])
            t_count= t_count + 1
            count_gen_pairing = count_gen_pairing + 1
    elif bid_type == 'GEN_PAIRING' and len(day_range)==0:
        date_from = cl.conv_d(row['From'])
        date_to = cl.conv_d(row['Until'])
        outputWriter.writerow([bid_type, crewid, date_from, date_to, avoid, daydict[''], daydict[''], max_times_roster, region, layover, max_lo_nt, transit, pax, bid_points])
        t_count = t_count + 1
        count_gen_pairing = count_gen_pairing + 1
    elif bid_type == 'GOLDEN_DO':
        date_from = cl.conv_d(row['From'])
        outputWriter.writerow([bid_type, crewid, date_from, bid_points])
        t_count = t_count + 1
        count_gof = count_gof + 1
    elif bid_type == 'SPEC_DO':
        date_from = cl.conv_d(row['From'])
        date_to = cl.conv_d(row['Until'])
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
        date_from = cl.conv_d(row['From'])
        date_to = cl.get_end_date_time(row['From'], row['Durn'])
        time_from = cl.conv_t(row['From'])
        time_to = date_to[1]
        outputWriter.writerow([bid_type, crewid, date_from, date_to[0], time_from, time_to,  bid_points])
        t_count = t_count + 1
        count_spec_time_off = count_spec_time_off + 1
    elif bid_type == 'QUAL_TIMEOFF':
        t_count = t_count + 1
        count_qual_time_off = count_qual_time_off + 1
    elif bid_type == 'GEN_TIMEOFF':
        dates = get_start_end_date_from_wom(row['Remarks'])


        t_count = t_count + 1
        count_gen_time_off = count_gen_time_off + 1
    elif bid_type == 'SPEC_PAIRING':
        t_count = t_count + 1
        count_spec_pairing = count_spec_pairing + 1
    else:
        t_count = t_count + 1
        continue

count_translated_bids = count_rule_relax + count_day_off + count_gen_pairing + count_gof


print("\n"+"Bids translated : " + str(count_translated_bids) + " out of " + str(t_count)+"\n"
      +"Generic pairing bids : "+ str(count_gen_pairing)+"\n"
      +"Golden day off bis : "+ str(count_gof)+"\n"
      +"Day off bids : "+ str(count_day_off)+"\n"
      +"Rule relaxations : "+ str(count_rule_relax)+"\n"
      +"Specific Time off bids : "+str(count_spec_time_off))
print("\n"+"Bids not translated : "+str(count_qual_time_off+count_gen_time_off+count_spec_pairing)+ " out of " + str(t_count)+"\n"
      +"Specific pairing bids : "+str(count_spec_pairing)+"\n"
      +"Quality time off bids : "+str(count_qual_time_off)+"\n"
      +"Generic time off bids : "+str(count_gen_time_off))

outputFile.close()






