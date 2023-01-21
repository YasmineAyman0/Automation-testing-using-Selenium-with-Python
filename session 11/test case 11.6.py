# test case 11.6 Scrolling
import time
import public as public
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.common.exceptions import WebDriverException

browser = webdriver.Chrome()
browser.get('http://localhost:80')
browser.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
browser.maximize_window()
time.sleep(8)
# 1)scroll down the page by pixels
# browser.execute_script("window.scrollBy(0,3000)","")
# value=browser.execute_script("return window.pageYOffset;")
# print("Number of pixels moved:",value)69

# 2)scroll down the page till the element is visible
# flag=browser.find_element(By.XPATH,"//img[@alt='Flag of Egypt']")
# browser.execute_script("arguments[0].scrollIntoView();",flag)
# value=browser.execute_script("return window.pageYOffset;")
# print("Number of pixels moved:",value)

# 3)scroll down the page till the end
browser.execute_script("window.scrollBy(0,document.body.scrollHeight)")
value = browser.execute_script("return window.pageYOffset;")
print("Number of pixels moved:", value)

# 4)scroll up to the starting position
browser.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
value = browser.execute_script("return window.pageYOffset;")
print("Number of pixels moved:", value)
browser.close()
