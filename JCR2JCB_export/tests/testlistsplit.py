import re
import pandas
from itertools import groupby
from operator import itemgetter


def get_days(s):  # returns dow in 3 letter day initials eg. 1 - Mon
    regex = r"dow:?\D+(\d+)"
    dow = re.findall(regex, s)  # returns array but for this case, array will have 1 element only i.e at index 0
    # s=dow[0]
    daydict = {"": "", "1": "Mon", "2": "Tue", "3": "Wed", "4": "Thu", "5": "Fri", "6": "Sat", "7": "Sun"}
    for i in range(0, len(s) - 1):
        m = s[i:i + 1]
        return daydict[m]



def group_consecutives(vals, step=1):
    """Return list of consecutive lists of numbers from vals (number list)."""
    run = []
    result = [run]
    expect = None
    for v in vals:
        if (v == expect) or (expect is None):
            run.append(v)
        else:
            run = [v]
            result.append(run)
        expect = v + step
    return result


def split_list(n):
    """will return the list index"""
    return [(x + 1) for x, y in zip(n, n[1:]) if y - x != 1]


def get_sub_list(my_list):
    """will split the list base on the index"""
    my_index = split_list(my_list)
    output = list()
    prev = 0
    for index in my_index:
        new_list = [x for x in my_list[prev:] if x < index]
        output.append(new_list)
        prev += len(new_list)
    output.append([x for x in my_list[prev:]])
    return output


def splitting(s):
    data = list(s)
    for k, g in groupby(enumerate(data), lambda ix: ix[0] - ix[1]):
        return map(itemgetter(1), g)


# my_list = [1, 3, 4, 7, 8, 10, 11, 13, 14]
# print (get_sub_list(my_list))

# print (get_days('dow:12 4567'))


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







def get_dow(s):
    if s is not None:
        regex = r"\s+"
        dow = re.sub(regex, '', s)
        print(dow)
        s_strip = dow.strip('dow:')
        print(s_strip)
        ranges1 = []
        print(ranges1)
        for j in s_strip:
            ranges1.append(int(j))
            print(j)
        return ranges1
    else:
        return ''


def get_days(s):  # returns dow in 3 letter day initials eg. 1 - Mon
    s_stripped = "".join(s.split())
    if 'dow' in s_stripped:
        # print("I'm in")
        regex = r"dow:?\D+(\d+)"
        dow = re.findall(regex, str_stripped)  # returns array but for this case, array will have 1 element only i.e at index 0
        dow_list = []
        for i in dow[0]:
            dow_list.append(int(i))
        return dow_list
    else:
        return []

def get_weeks(s):  # returns dow in 3 letter day initials eg. 1 - Mon
    s_stripped = "".join(s.split('.'))
    if 'wom' in s_stripped:
        # print("I'm in")
        regex = r"wom:?\D+(\d+)"
        dow = re.findall(regex,
                         s_stripped)  # returns array but for this case, array will have 1 element only i.e at index 0
        dow_list = []
        for i in dow[0]:
            dow_list.append(int(i))
        return dow_list
    else:
        return []

# print(group1(get_days('')))
# print(group1(get_days('dow:1367, wom:1234')))

# print(get_days('dow:1 3 67, wom:1234'))

str1= ''

reg = r"\s+"
s = re.findall(reg, str1)

str1= 'dow:1 3 67, wom:1234'
# str1=''
str_stripped ="".join(str1.split())
str_days = get_days(str1)
str_days_range = list(group(str_days)) # works for non empty list; returns empty list otherwise
str_grp = group_consecutives(str_days)
# str_grp2 = group1(str_days) # works for empty but not otherwise

str_weeks = get_weeks('dow:3....., wom:1..4')

print(str_weeks)

days = list(group(str_weeks))

days_range = pandas.date_range()

# print(str1)
# print(str_stripped)
# print(str_days)
# print(str_days_range,"working") # working one
# print(str_grp)
# print(str_grp2)



# print(group1(get_days('dow:1 3     67, wom:1234')))
# print(group1(get_days('dow:1234567')))
# print(group1(get_days('wom:4')))
#
#
# t = 'dow:1 3     67, wom:1234'
# s = group1([])
# print(s[0][0])
#
# reg = r"(?<=dow:).*?(?=wom)"
# reg2 = r"dow:?\D+(\d+)"
#
# print(re.findall(reg,t))
#
# print(''.split(','))





# print((dow_list[0].split()))

# final_list = list(group(dow_list))
#
# print(final_list)
#
# for i in range(0, len(final_list)):
#     day_from = final_list[i][0]
#     day_to = final_list[i][1]
#     print(get_days_2(str(day_from)), get_days_2(str(day_to)))


# print(final_list[1][0])
# print(final_list[1][1])


# print(get_days(final_list[0][0]))

daydict = {"": "", "1": "Mon", "2": "Tue", "3": "Wed", "4": "Thu", "5": "Fri", "6": "Sat", "7": "Sun"}

# print(daydict[''], 'empty working')