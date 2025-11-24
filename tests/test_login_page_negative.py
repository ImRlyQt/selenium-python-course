# Test case 2: Negative username test


import pytest
from selenium.webdriver.common.by import By

from Practice.page_objects.login_page import LoginPage


class TestNegativeScenarios:
    @pytest.mark.login
    @pytest.mark.negative
    @pytest.mark.parametrize("username, password, expected_error_message",
                             [("incorrectUser", "Password123", "Your username is invalid!"),
                              ("student", "incorrectPassword", "Your password is invalid!")])
    def test_negative_login(self, driver, username, password, expected_error_message):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.execute_login(username, password)

        # 5. Verify error message is displayed
        error_message_locator = driver.find_element(By.ID, "error")
        assert error_message_locator.is_displayed(), "Error is not displayed but should be"

        # 6. Verify error message text is Your username is invalid!
        error_message = error_message_locator.text
        assert error_message == expected_error_message, "Error message is not expected"
