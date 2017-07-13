# time testing
import datetime
import calendar
import time
from datetime import timedelta
import cleaning_module as cl


def get_end_date_time(start, durn):
    stripped_time = time.strptime(start, '%d%b%Y %H%M') #returns tuple
    start_date = datetime.datetime(stripped_time.tm_year,
                                   stripped_time.tm_mon,
                                   stripped_time.tm_mday,
                                   stripped_time.tm_hour,
                                   stripped_time.tm_min,
                                   stripped_time.tm_sec)

    end_date_time = start_date + timedelta(hours=durn)

    end_date_time_stripped = time.strptime(str(end_date_time),'%Y-%m-%d %H:%M:%S')

    end_date = time.strftime('%d/%m/%y', end_date_time_stripped)
    end_time = time.strftime('%H:%M',end_date_time_stripped)
    return [end_date, end_time]


def get_start_end_date(start, x, y):
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


print(get_start_end_date('06AUG2017 0600', 2, 3)) # testing git commit

print(get_start_end_date('06AUG2017 0600', 1, 1))

print(get_start_end_date('06AUG2017 0600', 1, 4))


# print(cl.conv_d('05AUG2017 0600'))

# print(cl.conv_t('05AUG2017'))



# A combination of a date and a time. Attributes: year, month, day, hour, minute, second, microsecond, and tzinfo.