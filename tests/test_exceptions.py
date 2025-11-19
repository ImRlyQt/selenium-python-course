import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class TestExceptions:

    @pytest.mark.exceptions
    def test_no_such_element_exception(self, driver):
        # 1. Open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        # 2. Click Add button
        add_button_locator = driver.find_element(By.ID, "add_btn")
        add_button_locator.click()

        # 3. Verify Row 2 input field is displayed
        wait = WebDriverWait(driver, 10)
        row_2_input_element = wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@id='row2']/input")))
        assert row_2_input_element.is_displayed(), "Row 2 input should be displayed but is not"

    @pytest.mark.exceptions
    @pytest.mark.debug
    def test_element_not_interactable_exception(self, driver):
        # 1. Open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        # 2. Click Add button
        add_button_locator = driver.find_element(By.ID, "add_btn")
        add_button_locator.click()

        # 3. Wait for the second row to load
        wait = WebDriverWait(driver, 10)
        row_2_input_element = wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@id='row2']/input")))

        # 4. Type text into the second input field
        row_2_input_element.send_keys("Żurek")

        # 5. Push Save button using locator By.name(“Save”)
        driver.find_element(By.XPATH, "//div[@id='row2']/button[@name='Save']").click()

        # 6. Verify text saved
        confirmation_element = driver.find_element(By.ID, "confirmation")
        confirmation_message = confirmation_element.text
        assert confirmation_message == "Row 2 was saved", "Confirmation message is not expected"
