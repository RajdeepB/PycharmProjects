import re


x = [2, 4, 7]

def group(L):
    first = last = L[0]
    for n in L[1:]:
        if n - 1 == last: # Part of the group, bump the end
            last = n
        else: # Not part of the group, yield current group and start a new
            yield first, last
            first = last = n
    yield first, last # Yield the last group

print(list(group(x)))

def get_days(s): # returns dow in 3 letter day initials eg. 1 - Mon
    regex = r"dow:?\D+(\d+)"
    dow = re.findall(regex, s) # returns array but for this case, array will have 1 element only i.e at index 0
    s=dow[0]
    daydict ={"1":"Mon","2":"Tue","3":"Wed","4":"Thu","5":"Fri","6":"Sat","7":"Sun"}
    for i in range (0,len(s)):
        m=s[i:i+1]
        return daydict[m]


