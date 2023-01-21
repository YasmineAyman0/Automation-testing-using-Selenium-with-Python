# test case 8.1 alerts 1
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv = Service("E:\Interviews\Automation\python\chromedriver.exe")
browser = webdriver.Chrome(service=serv)
browser.get("http://the-internet.herokuapp.com/javascript_alerts")
# browser.maximize_window()

# opens alert window
browser.find_element(By.XPATH, "//button[@onclick='jsPrompt()']").click()
time.sleep(6)
alertwindow = browser.switch_to.alert
print(alertwindow.text)
alertwindow.send_keys("welcome")
time.sleep(5)
alertwindow.accept()  # clicking ok before close the alert window
# alertwindow.dismiss() #clicking cancel before close the alert window
