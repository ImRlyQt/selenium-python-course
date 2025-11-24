import pytest

from Practice.page_objects.logged_in_successfully import LoggedInSuccessfullyPage
from Practice.page_objects.login_page import LoginPage


class TestPositiveScenarios:

    @pytest.mark.login
    @pytest.mark.positive
    def test_positive_login(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.execute_login("student", "Password123")
        login_in_page = LoggedInSuccessfullyPage(driver)
        assert login_in_page.expected_url == login_in_page.current_url, "Actual URL is not the same as expected"
        assert login_in_page.header == "Logged In Successfully", "Header is not expected"
        assert login_in_page.is_logout_button_displayed(), "Logout button should be visible"
