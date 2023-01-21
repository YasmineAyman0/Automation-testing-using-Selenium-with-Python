# test case 11.5 Slider element
import time
import public as public
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('http://localhost:80')
browser.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")
browser.maximize_window()

min_slider = browser.find_element(By.XPATH, "//span[1]")
max_slider = browser.find_element(By.XPATH, "//span[2]")

print("Default location of sliders")

print(min_slider.location)
print(max_slider.location)

act = ActionChains(browser)
act.drag_and_drop_by_offset(min_slider, 100, 0).perform()
act.drag_and_drop_by_offset(max_slider, -200, 0).perform()

print("Location of sliders after moving")
print(min_slider.location)
print(max_slider.location)
browser.close()
