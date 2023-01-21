# test case 7.3 handle links
import time
import requests as requests
from telnetlib import EC
from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

serv = Service("E:\Interviews\Automation\python\chromedriver.exe")
browser = webdriver.Chrome(service=serv)
browser.get("https://demo.opencart.com/index.php?route=product/category&language=en-gb&path=33")
# browser.maximize_window()
time.sleep(20)
search = Select(browser.find_element(By.XPATH, "//select[@id='input-sort']"))
# search_try=Select(search)
# ____________________select option from dropdown list___________________________
# search.select_by_visible_text("Name (A - Z)")

# ____________________select all options from dropdown list______________________

# alloptions=search.options
# print(len(alloptions))
# for opt in alloptions:
#   print(opt.text)

# ________select option from dropdown list without using built in function_______

# Approach 1
# for opt in alloptions:
#   if opt=="Name (A - Z)":
#      opt.click()
#     break


# Approach 2
alloptions = browser.find_elements(By.XPATH, "//select[@id='input-sort']")
print(len(alloptions))
time.sleep(10)
