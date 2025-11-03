# open browser
import time

from selenium import webdriver

driver = webdriver.Chrome()
time.sleep(2)

driver.get("https://practicetestautomation.com/practice-test-login/")

time.sleep(5)
