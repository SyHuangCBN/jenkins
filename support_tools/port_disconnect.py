# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 16:18:24 2018

@author: Gerben_Chen
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import time, re, os
import argparse

HELP_EPILOG = '''
Example use:

 python port_disconnect.py -n <mv1-1-1>

'''
'''
Read command-line arguments, return a simple configuration for running tests.
'''
parser = argparse.ArgumentParser(description='Control Console Switch Disconnect Port to Slove Board In Use',
                                                                 usage='wifisuite [options...]',
                                                                 formatter_class=argparse.RawDescriptionHelpFormatter,
                                                                 epilog=HELP_EPILOG)
parser.add_argument('-n', '--board', metavar='', type=str, default=None, help='Board Name')

args = parser.parse_args()

match = re.search('mv(\d+)-(\d+)-(\d+)', args.board)
bf_station = match.group(2)
board_number = match.group(3)
if bf_station == "1" and int(board_number) < 13:
    ip_address = "172.16.1.241"
    atom = int(board_number)*2
    arm = atom - 1
elif bf_station == "1" and 12 < int(board_number) < 25:
    ip_address = "172.16.1.197"
    atom = (int(board_number)*2)-24
    arm = atom - 1
elif bf_station == "1" and 24 < int(board_number) < 37:
    ip_address = "172.16.1.194"
    atom = (int(board_number)*2)-48
    arm = atom - 1
elif bf_station == "2":
    ip_address = "172.16.1.217"
    atom = int(board_number)*2
    arm = atom - 1
elif bf_station == "3":
    ip_address = "172.16.1.215"
    atom = int(board_number)*2
    arm = atom - 1

options = webdriver.FirefoxOptions()
options.set_headless()
options.add_argument('--disable-gpu')
driver = webdriver.Firefox(firefox_options=options)
driver.implicitly_wait(15)
#driver.get(url)
#driver = webdriver.Firefox()
driver.get("http://%s/nti/login.asp" % ip_address)
driver.find_element_by_name("UserName").click()
driver.find_element_by_name("UserName").clear()
driver.find_element_by_name("UserName").send_keys("root")
driver.find_element_by_name("Password").click()
driver.find_element_by_name("Password").clear()
driver.find_element_by_name("Password").send_keys("nti")
driver.find_element_by_name("ok").click()
driver.find_element_by_id("DisconPort").click()
driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Disconnect Port:'])[1]/following::option[%s]" % arm).click()
driver.find_element_by_name("discon").click()
time.sleep(10)
Select(driver.find_element_by_id("DisconPort")).select_by_visible_text("Port2")
driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Disconnect Port:'])[1]/following::option[%s]" % atom).click()
driver.find_element_by_name("discon").click()
driver.quit()