import cleaning_module as cl
import re

# print(cl.conv_t('24-Jul-17'))

s1 = '24-Jul-17'
s2 = '07JUN17 1005'
s3 = '1159'
s4 = '600'

regex = r"\w+"
matches = re.search(regex,s1)

# print(s1.strip('-'))

# print(s3[0:2])

print(s2[-1:-3])


# def get_start_end_date_time(startdate, enddate, duration):


# def get_