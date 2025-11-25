import time
from logging import exception

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from Practice.page_objects.exceptions_page import ExceptionsPage


class TestExceptions:
    @pytest.mark.exceptions
    def test_no_such_element_exception(self, driver):
        exceptions_page = ExceptionsPage(driver)
        exceptions_page._open()
        exceptions_page._add_second_row()
        assert exceptions_page._is_row_2_displayed(), "Row 2 input should be displayed but is not"

    @pytest.mark.exceptions
    def test_element_not_interactable_exception(self, driver):
        exceptions_page = ExceptionsPage(driver)
        exceptions_page._open()
        exceptions_page._add_second_row()
        exceptions_page._row_2_input_text("żurek")
        assert exceptions_page._get_confirmation_message() == "Row 2 was saved", "Confirmation message is not expected"

    @pytest.mark.exceptions
    def test_invalid_element_state_exception(self, driver):
        exceptions_page = ExceptionsPage(driver)
        exceptions_page._open()
        exceptions_page._row_1_input_text("żurek")
        assert exceptions_page._get_confirmation_message() == "Row 1 was saved", "Confirmation message is not expected"

    @pytest.mark.exceptions
    def test_stale_element_reference_exception(self, driver):
        exceptions_page = ExceptionsPage(driver)
        exceptions_page._open()
        exceptions_page._add_second_row()
        assert not exceptions_page._are_instructions_displayed(), "Instruction text element should not be displayed"

    @pytest.mark.debug
    @pytest.mark.exceptions
    def test_timeout_exception(self, driver):
        exceptions_page = ExceptionsPage(driver)
        exceptions_page._open()
        exceptions_page._add_second_row()
        assert exceptions_page._is_row_2_displayed(), "Row 2 input should be displayed but is not"

