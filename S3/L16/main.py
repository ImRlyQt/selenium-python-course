import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# open browser
driver = webdriver.Chrome()
time.sleep(1)
# 1. Open page
driver.get("https://practicetestautomation.com/practice-test-login/")
time.sleep(1)

# 2. Type username student into Username field
username_locator = driver.find_element(By.ID, "username")

# 3. Type password Password123 into Password field
password_locator = driver.find_element(By.NAME, "password")

# 4. Push Submit button
submit_button_locator = driver.find_element(By.XPATH, "//button[@class='btn']")

# 5. Verify new page URL contains practicetestautomation.com/logged-in-successfully/

# 6. Verify new page contains expected text ('Congratulations' or 'successfully logged in')
logged_in_text_locator = driver.find_element(By.TAG_NAME, "h1")

# 7. Verify button Log out is displayed on the new page
logout_button_locator = driver.find_element(By.LINK_TEXT, "Log out")
