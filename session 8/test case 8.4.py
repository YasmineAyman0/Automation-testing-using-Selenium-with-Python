# test case 8.4 frames/Iframes

# handle frames
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote import switch_to

serv = Service("E:\Interviews\Automation\python\chromedriver.exe")
browser = webdriver.Chrome(service=serv)

browser.get("https://demo.automationtesting.in/Frames.html")

outerframe = browser.find_element(By.XPATH, "//iframe[@id='singleframe']")
switch_to.frame(outerframe)
time.sleep(7)
innerframe = browser.find_element(By.XPATH,
                                  "//iframe[normalize-space()='<p>Your browser does not support iframes.</p>']")
switch_to.frame(innerframe)
time.sleep(6)
# To go back again in the outer frame there is a command only in selenium 4 instead of go back to the webpage
browser.switch_to.parent_frame()
