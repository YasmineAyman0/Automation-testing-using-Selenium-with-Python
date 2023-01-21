# test case 11.3 double click
import time

import public as public
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('http://localhost:80')
browser.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_ev_ondblclick3")
browser.maximize_window()
browser.switch_to.frame("field1")
field1 = browser.find_element(By.XPATH, "//input[@id='field1']")
field1.clear()
field1.send_keys("welcome")
button = browser.find_element(By.XPATH, "//button[@ondblclick='myFunction()']")
act = ActionChains(browser)
act.double_click(button).perform()
