from selenium import webdriver
import pytest


@pytest.fixture()
def driver():
    print("Creating chrome driver")
    # my_driver = webdriver.Chrome() #no kurwa odpala chroma cnie
    my_driver = webdriver.Firefox() #no kurwa odpala firefox co nie
    yield my_driver
    print("\nClosing chrome driver")
    my_driver.quit()
