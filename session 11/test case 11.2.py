# test case 11.2 right click
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('http://localhost:80')
browser.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
browser.maximize_window()
time.sleep(5)
button = browser.find_element(By.XPATH, "//span[@class='context-menu-one btn btn-neutral']")

act = ActionChains(browser)
act.context_click(button).perform()
browser.close()
