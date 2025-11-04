# Test case 2: Negative username test
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestNegativeScenarios:

    @pytest.mark.negative
    def test_negative_username(self):
        # 1. Open page
        driver = webdriver.Chrome()
        driver.get("https://practicetestautomation.com/practice-test-login/")

        # 2. Type username incorrectUser into Username field
        username_locator = driver.find_element(By.ID, "username")
        username_locator.send_keys("incorrectUser")

        # 3. Type password Password123 into Password field
        password_locator = driver.find_element(By.NAME, "password")
        password_locator.send_keys("Password123")

        # 4. Push Submit button
        submit_button_locator = driver.find_element(By.XPATH, "//button[@class='btn']")
        submit_button_locator.click()
        time.sleep(5)
        # 5. Verify error message is displayed
        # 6. Verify error message text is Your username is invalid!
