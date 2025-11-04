# Test case 3: Negative password test
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestNegativeScenarios:
    @pytest.mark.login
    @pytest.mark.negative
    @pytest.mark.negative_password
    def test_negative_username(self):
        # 1. Open page
        driver = webdriver.Chrome()
        driver.get("https://practicetestautomation.com/practice-test-login/")

        # 2. Type username student into Username field
        username_locator = driver.find_element(By.ID, "username")
        username_locator.send_keys("student")

        # 3. Type password incorrectPassword into Password field
        password_locator = driver.find_element(By.NAME, "password")
        password_locator.send_keys("incorrectPassword")

        # 4. Push Submit button
        submit_button_locator = driver.find_element(By.XPATH, "//button[@class='btn']")
        submit_button_locator.click()

        # 5. Verify error message is displayed
        error_message_locator = driver.find_element(By.ID, "error")
        assert error_message_locator.is_displayed(), "Error is not displayed but should be"

        # 6. Verify error message text is Your password is invalid!
        error_message = error_message_locator.text
        assert error_message == "Your password is invalid!", "Error message is not expected"
