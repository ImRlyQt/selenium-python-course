import time
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

    @pytest.mark.exceptions
    def test_invalid_element_state_exception(self, driver):
        # 1. Open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        # 2. Clear input field
        row_1_edit_button = driver.find_element(By.ID, "edit_btn")
        row_1_edit_button.click()
        row_1_input_element = driver.find_element(By.XPATH, "//div[@id='row1']/input")
        wait = WebDriverWait(driver, 10)
        wait.until(ec.element_to_be_clickable(row_1_input_element))
        row_1_input_element.clear()

        # 3. Type text into the input field
        row_1_input_element.send_keys("żurek")
        row_1_save_button = driver.find_element(By.ID, "save_btn")
        row_1_save_button.click()

        # 4. Verify text changed
        confirmation_element = wait.until(ec.visibility_of_element_located((By.ID, "confirmation")))
        confirmation_message = confirmation_element.text
        assert confirmation_message == "Row 1 was saved", "Confirmation message is not expected"

    @pytest.mark.exceptions
    def test_stale_element_reference_exception(self, driver):
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        # Push add button
        driver.find_element(By.ID, "add_btn").click()

        # Verify instruction text element is no longer displayed
        wait = WebDriverWait(driver, 10)
        assert wait.until(ec.invisibility_of_element_located(
            (By.ID, "instructions"))), "Instruction text element should not be displayed"

    @pytest.mark.exceptions
    @pytest.mark.debug
    def test_timeout_exception(self, driver):
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        # Click Add button
        driver.find_element(By.ID, "add_btn").click()

        # Wait for 3 seconds for the second input field to be displayed
        wait = WebDriverWait(driver, 5.1)
        row_2_input_element = wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@id='row2']/input")), "Failed waiting for Row 2 input to be visible")
        # Verify second input field is displayed
        assert row_2_input_element.is_displayed()