import pytest


from selenium import webdriver
import pytest

from selenium.webdriver.chrome.service import Service as ChromeService

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

@pytest.fixture
def set_up():

    driver.maximize_window()

    yield driver

    driver.quit()


def test_one(set_up):

    driver.get("https://www.devpropvivo.com")

    s = "test"

    reverse_string = s[::-1]

    print(reverse_string)
#       
# def test_reverse_string(s):
#     return s == s[::-1]
#
#
#
# call_function = test_reverse_string(s)
#
# print(call_function)