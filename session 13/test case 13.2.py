# test case 13.2 capture screenshot from dropdown list
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
# browser.save_screenshot("E:\\Interviews\\Automation\\python\\python testing files\\session 13\\homepage.png")
# browser.find_element(By.XPATH,"//button[@type='submit']").click()
# browser.save_screenshot(os.getcwd()+"\\homepage.png")
# browser.get_screenshot_as_file(os.getcwd()+"\\homepagefile.png")
# browser.switch_to.new_window('tab')
browser.switch_to.new_window('window')
browser.get("https://www.facebook.com/")
browser.quit()
