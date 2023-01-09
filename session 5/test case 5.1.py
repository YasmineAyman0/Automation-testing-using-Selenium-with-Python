import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('http://localhost:80')
browser.get("https://admin-demo.nopcommerce.com/admin/")
browser.maximize_window()
#__________________________Application commands______________________________
#print(browser.title)
#print(browser.current_url)
#print(browser.page_source)
#---------------------------Conditional commands-----------------------------
#searchbox=browser.find_element(By.XPATH,"//input[@placeholder='Search']")
#print(searchbox.is_displayed())
#print(searchbox.is_enabled())
#____________________________Browser commands________________________________
#browser.close()
#browser.quit()
#____________________________Navigational commands___________________________
#After i open nop-commerce website, I would like to open facebook and go back again to nop-commerce website
browser.get("https://www.facebook.com/")
browser.back() #nop-commerce
browser.forward() #facebook
browser.refresh() #this automatically will reload the page
time.sleep(5)