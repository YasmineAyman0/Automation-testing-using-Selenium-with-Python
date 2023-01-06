#test case 2.1
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
browser = webdriver.Chrome()
browser.get('http://localhost:80')
browser.get("https://www.facebook.com")
#browser.find_element(By.CSS_SELECTOR,"input#email").send_keys("abc")
browser.find_element(By.CSS_SELECTOR,"input.inputtext").send_keys("abc@gmail.com")
browser.maximize_window()
time.sleep(10)