# test case 13.3 handle cookies
import time
import public as public
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
import os

browser = webdriver.Chrome()
browser.implicitly_wait(6)
browser.get('http://localhost:80')
browser.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
browser.maximize_window()

# capture cookies from the browser
cookies = browser.get_cookies()
print("size of cookies:", len(cookies))

# print details of all cookies
# for c in cookies:
#   print(c.get('name'),":",c.get('value'))

# Add a new cookie to the browser
browser.add_cookie({"name": "MyCookie", "value": "123456"})
cookies = browser.get_cookies()
print("size of cookies after adding a new one:", len(cookies))

# Delete specific cookie from the browser
browser.delete_cookie("MyCookie")
cookies = browser.get_cookies()
print("size of cookies after deleted one:", len(cookies))

# Delete all cookies
browser.delete_all_cookies()
cookies = browser.get_cookies()
print("size of cookies after deleted all cookies:", len(cookies))
browser.quit()
