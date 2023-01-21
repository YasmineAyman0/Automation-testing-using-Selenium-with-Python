# test case 7.2 handle links
import time
import requests as requests
from telnetlib import EC
from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

serv = Service("E:\Interviews\Automation\python\chromedriver.exe")
browser = webdriver.Chrome(service=serv)
browser.get("http://www.deadlinkcity.com/")
browser.maximize_window()
time.sleep(20)
browser.find_element(By.LINK_TEXT, "Logout").click()
time.sleep(10)
