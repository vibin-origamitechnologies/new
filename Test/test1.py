

from selenium import webdriver
import time
#driver = webdriver.Chrome()
driver = webdriver.Chrome("..\Drivers\chromedriver.exe")

driver.set_page_load_timeout(10)
driver.get("http://google.com")
driver.maximize_window()
driver.refresh()
time.sleep(5)
driver.quit()
