# test case 8.5 Browser windows
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote import switch_to
from selenium import webdriver

serv = Service("E:\Interviews\Automation\python\chromedriver.exe")
browser = webdriver.Chrome(service=serv)

browser.get("https://www.freecodecamp.org/news/list-index-out-of-range-python-error-solved/")

# __________________________Approach 1 print single page id____________________________

# windowid = browser.current_window_handle
# print(windowid) #With every run the new window id will be printed each time
# CDwindow-F97F6008C37BC91082BB47C83A9A099C

# __________________________Approach 2 print multiple page id__________________________

browser.find_element(By.XPATH, "//span[normalize-space()='free 3,000-hour curriculum']").click()
# time.sleep(5)
# windowids = browser.window_handles
# parentwindowid = windowids[0] #CDwindow-B6A2BE8C6C4E7679956EF0ABA317CF04
# childwindowid = windowids[1]  #CDwindow-6E3FF648E84AC1CD9C0FFAAD812BCD31
# time.sleep(5)
# print(parentwindowid, childwindowid)
# __________________________Approach 3 print multiple page id using for loop____________
# time.sleep(5)
# windowid = browser.window_handles
# for winid in windowid:
#    browser.switch_to.window(winid)
#   print(browser.title)
# browser.close()

# ____________________________Close specific window in the browser________________________
windowid = browser.window_handles
time.sleep(5)
for winid in windowid:
    browser.switch_to.window(winid)
    if browser.title == "List Index Out of Range – Python Error [Solved]":
        browser.close()
