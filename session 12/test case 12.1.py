# test case 12.1 select, copy, Tab and paste
import time
import public as public
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.common.exceptions import WebDriverException

browser = webdriver.Chrome()
browser.implicitly_wait(6)
browser.get('http://localhost:80')
browser.get("https://text-compare.com/")
browser.maximize_window()
input1 = browser.find_element(By.XPATH, "//textarea[@id='inputText1']")
input2 = browser.find_element(By.XPATH, "//textarea[@id='inputText2']")

input1.send_keys("welcome to selenium")
time.sleep(5)
act = ActionChains(browser)
# ctrl+a
act.key_down(Keys.CONTROL)
act.send_keys("a")
act.key_up(Keys.CONTROL)
act.perform()

# ctrl+c
act.key_down(Keys.CONTROL)
act.send_keys("c")
act.key_up(Keys.CONTROL)
act.perform()

# Tab
act.send_keys(Keys.TAB).perform()

# ctrl+v
act.key_down(Keys.CONTROL)
act.send_keys("v")
act.key_up(Keys.CONTROL)
act.perform()
