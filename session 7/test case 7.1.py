# test case 7.1 checkboxes
import time
from telnetlib import EC
from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

serv = Service("E:\Interviews\Automation\python\chromedriver.exe")
browser = webdriver.Chrome(service=serv)
browser.get("https://itera-qa.azurewebsites.net/home/automation")
browser.maximize_window()
# 1)select specific checkbox
# browser.find_element(By.XPATH,"//input[@id='monday']").click()
# 2)select all the checkboxs
time.sleep(30)
checkboxes = browser.find_elements(By.XPATH, "//input[@type='checkbox' and contains(@id,'day')]")
print(len(checkboxes))
# Approach 1
# for i in range(len(checkboxes)):
#   checkboxes[i].click()

# Approach 2
# for checkbox in checkboxes:
#   checkbox.click()
# _______________________select multiple checkboxes_______________________
# for checkbox in checkboxes:
#   weekname = checkbox.get_attribute('id')
#  if weekname == 'monday' or weekname == 'sunday':
#     checkbox.click()
# _______________________select last 2 checkboxes__________________________
# for i in range(len(checkboxes)-2,len(checkboxes)):#range from (5 to 7)
#   checkboxes[i].click()

# _______________________select first 2 checkboxes__________________________
# for i in range(len(checkboxes)):  # range from (0 to 2)
#   if i < 2:
#      checkboxes[i].click()

# _______________________clearing all the checkboxes__________________________
time.sleep(4)
for checkbox in checkboxes:
    if checkbox.is_selected():
        checkbox.click()
time.sleep(7)
