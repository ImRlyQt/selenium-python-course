# Test case 2: Negative username test
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestNegativeScenarios:

    def test_negative_username(self):

        # 1. Open page
        driver = webdriver.Chrome()
        driver.get("https://practicetestautomation.com/practice-test-login/")

        # 2. Type username incorrectUser into Username field
        username_locator = driver.find_element(By.ID, "username")
        username_locator.send_keys("student")


        # 3. Type password Password123 into Password field
        # 4. Push Submit button
        # 5. Verify error message is displayed
        # 6. Verify error message text is Your username is invalid!
