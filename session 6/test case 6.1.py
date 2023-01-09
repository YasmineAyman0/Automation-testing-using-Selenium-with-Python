# test case 6.1 implicit wait
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('http://localhost:80')
browser.get("https://www.google.com/")
browser.implicitly_wait(10)
browser.maximize_window()

searchbox = browser.find_element(By.NAME, "q")
searchbox.send_keys("selenium")
searchbox.submit()

browser.implicitly_wait(100)
