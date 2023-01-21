# test case 8.2 alerts 2
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv = Service("E:\Interviews\Automation\python\chromedriver.exe")
browser = webdriver.Chrome(service=serv)
browser.get("https://mypage.rediff.com/")
# browser.maximize_window()

# opens alert window
time.sleep(5)
browser.find_element(By.XPATH, "//input[@value=' Go ']").click()
time.sleep(6)
browser.switch_to.alert.accept()
browser.close()
