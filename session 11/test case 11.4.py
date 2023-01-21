# test case 11.4 Drag and drop
import time
import public as public
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('http://localhost:80')
browser.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
browser.maximize_window()
Madrid = browser.find_element(By.ID, "box7")
Spain = browser.find_element(By.ID, "box107")
act = ActionChains(browser)
act.drag_and_drop(Madrid, Spain).perform()
browser.close()
