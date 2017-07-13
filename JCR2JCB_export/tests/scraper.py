# import re
# import time
# import calendar
# import cProfile
# import csv
from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import Select
# from selenium.common.exceptions import NoSuchElementException
# from selenium.common.exceptions import NoAlertPresentException
# from selenium.webdriver.common.by import By
# import unittest, time, re
import requests


a = requests.get('http://whed.net/home.php')

# print(a.text)

driver = webdriver.Firefox()



