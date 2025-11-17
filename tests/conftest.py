from selenium import webdriver
import pytest


@pytest.fixture()
def driver():
    print("Creating chrome driver")
    my_driver = webdriver.Chrome()
    yield my_driver
    print("\nClosing chrome driver")
    my_driver.quit()
