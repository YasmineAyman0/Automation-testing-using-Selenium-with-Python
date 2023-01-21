# test case 8.2 alerts 3
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv = Service("E:\Interviews\Automation\python\chromedriver.exe")
browser = webdriver.Chrome(service=serv)
# Access website with username and password through the alert window
browser.get("http://admin:admin@the-internet.herokuapp.com/basic_auth")
browser.maximize_window()
time.sleep(7)
