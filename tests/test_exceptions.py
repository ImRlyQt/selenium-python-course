# Test case 1: NoSuchElementException
# Open page
# Click Add button
# Verify Row 2 input field is displayed
# Row 2 doesn’t appear immediately. This test will fail with org.openqa.selenium.NoSuchElementException without proper wait

import pytest
from selenium.webdriver.common.by import By


class TestExceptions:

    @pytest.mark.exeptions
    def test_no_suc_element_exception(self, driver):
        # 1. Open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        # 2. Click Add button
        add_button_locator = driver.find_element(By.ID, "add_btn")
        add_button_locator.click()

        # 3. Verify Row 2 input field is displayed
        row_2_input_locator = driver.find_element(By.XPATH, "//div[@id='row2']/input")
        assert row_2_input_locator.is_displayed(), "Row 2 input should be displayed but is not"

