import re
import time
import calendar
import cProfile
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.by import By
import unittest, time, re


def get_days(s): # returns dow in 3 letter day initials eg. 1 - Mon
    regex = r"dow:?\D+(\d+)"
    dow = re.findall(regex, s) # returns array but for this case, array will have 1 element only i.e at index 0
    s=dow[0]
    daydict ={"1":"Mon","2":"Tue","3":"Wed","4":"Thu","5":"Fri","6":"Sat","7":"Sun"}
    for i in range (0,len(s)):
        m=s[i:i+1]
        print(daydict[m])


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

def convert_date(d):
    final = time.strptime(d, "%d-%b-%y")
    final2 = time.strftime("%d/%m/%y",final)
    return str(final2)

def convert_date2(d):
    final = time.strptime(d, "%d%b%y %H%M")
    final2 = time.strftime("%d/%m/%y",final)
    return str(final2)

def get_avoid(d):
    if str(d) in ['AGT','AST','ATDA']:
        return True
    else:
        return False


def setUp(self):
    self.driver = webdriver.Chrome(executable_path='D:\chromedriver_win32\chromedriver.exe')
    self.driver.implicitly_wait(30)
    self.base_url = "https://crewportal-test.airnz.co.nz/site/"
    self.verificationErrors = []
    self.accept_next_alert = True
    driver = self.driver
    driver.get(self.base_url)
    driver.find_element_by_id("IDToken1").clear()
    driver.find_element_by_id("IDToken1").send_keys("baruar")
    driver.find_element_by_id("IDToken2").clear()
    driver.find_element_by_id("IDToken2").send_keys("Password1")
    driver.find_element_by_name("Login.Submit").click()


def fillGofBids(self, crew_id, gof_date, points):
    driver = self.driver
    self.base_url = "https://crewportal-test.airnz.co.nz/site/crewweb/#/ViewPlacedBids"
    driver.get(self.base_url)
    driver.find_element_by_css_selector("a.dropdown-toggle.menu-expander").click()
    driver.find_element_by_css_selector("a.content.menu-icon-ambassador > span").click()
    driver.find_element_by_xpath("//input[@type='text']").clear()
    driver.find_element_by_xpath("//input[@type='text']").send_keys(crew_id)
    driver.find_element_by_css_selector("button.btn.btn-primary").click()
    driver.find_element_by_css_selector("i.icon-create-bid").click()
    driver.find_element_by_link_text("Day(s) / Time Off").click()
    Select(driver.find_element_by_id("bidAccountTypes")).select_by_visible_text("Golden Day Off")
    driver.find_element_by_id("dateIntervalFrom").send_keys(gof_date)
    Select(driver.find_element_by_id("bidPoints")).select_by_visible_text(points)
    driver.find_element_by_id("placeBidButton").click()



csvFile = open('D:\MHCC_R4_Bids.csv')

csvDReader = csv.DictReader(csvFile)

setUp()

for row in csvDReader:
    bid_type = row['.']
    num = row['Number']
    avoid = str(get_avoid(row['Pref Type']))
    max_times_roster = setMaxTimesRoster(row['Rqd'])
    bid_points = setPoints((int(row['Wt'])))
    layover = row['Tod/Port']
    region = row['Rgn']
    try:
        if bid_type in ('SPEC_PAIRING','SPEC_TIMEOFF'):
            date_from = convert_date2(row['From'])
            date_to = convert_date2(row['Until'])
        elif bid_type in ('GEN_PAIRING','SPEC_DO','GEN_TIMEOFF'):
            date_from = convert_date(row['From'])
            date_to = convert_date(row['Until'])
        elif bid_type in ('GOLDEN_DO'):
            date_from = convert_date(row['From'])
            date_to =''
            # fillGofBids(self=, )
        else:
            date_from = ''
            date_to = ''
    except ValueError:
        print('value error')
    bid_object = [num, avoid, date_from, date_to, max_times_roster, bid_points, layover, region]
    print(','.join(bid_object))