from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from Practice.page_objects.base_page import BasePage


class ExceptionsPage(BasePage):
    __url = "https://practicetestautomation.com/practice-test-exceptions/"
    __add_button_locator = (By.ID, "add_btn")
    __edit_button_locator = (By.ID, "edit_btn")
    __row_1_save_button = (By.XPATH, "//div[@id='row1']/button[@name='Save']")
    __row_2_save_button = (By.XPATH, "//div[@id='row2']/button[@name='Save']")
    __row_1_input_element = (By.XPATH, "//div[@id='row1']/input")
    __row_2_input_element = (By.XPATH, "//div[@id='row2']/input")
    __confirmation_element = (By.ID, "confirmation")
    __instructions_element = (By.ID, "instructions")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def _open(self):
        super()._open_url(self.__url)

    def _add_second_row(self):
        super()._click(self.__add_button_locator)
        super()._wait_until_element_is_visible(self.__row_2_input_element)

    def _is_row_2_displayed(self) -> bool:
        return super()._is_displayed(self.__row_2_input_element)

    def _row_2_input_text(self, text: str):
        super()._type(self.__row_2_input_element, text)
        super()._click(self.__row_2_save_button)

    def _row_1_input_text(self, text: str):
        super()._click(self.__edit_button_locator)
        super()._clear(self.__row_1_input_element)
        super()._type(self.__row_1_input_element, text)
        super()._click(self.__row_1_save_button)


    def _get_confirmation_message(self) ->str:
        return super()._get_text(self.__confirmation_element, time=3)

    def _are_instructions_displayed(self) -> bool:
        return super()._is_displayed(self.__instructions_element)

