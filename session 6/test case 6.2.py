# test case 6.1 explicit wait
import time
from telnetlib import EC
from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

# browser.get('http://localhost:80')
# browser.implicitly_wait(10)
serv = Service("E:\Interviews\Automation\python\chromedriver.exe")
browser = webdriver.Chrome(service=serv)
mywait = WebDriverWait(browser, 10, ignored_exceptions=[NoSuchElementException,
                                                        ElementNotVisibleException,
                                                        ElementNotSelectableException,
                                                        Exception
                                                        ]
                       )
browser.get("https://www.google.com/")
browser.maximize_window()
searchbox = browser.find_element(By.NAME, "q")
searchbox.send_keys("selenium")
searchbox.submit()
time.sleep(50)
searchlink = mywait.until(EC.presence_of_element_located(By.XPATH, "//h3[text()='selenium']"))
searchlink.click()
# browser.find_element(By.XPATH,"//h3[text()='selenium']").click()
browser.back()
time.sleep(50)
browser.quit()
