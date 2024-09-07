

import pytest

from selenium import webdriver

email_id = [vipul@123gmail.com, vipul@234gamil.com, vipul@456gmail.com ]


@pytest.mark.parametrize("input",email_id)
def email_id(input):

    driver = webdriver.chrome()
    import By
    driver.get("http://www.test.com")

    email_id = driver.find_element(by=By.XPATH, value="test")
    email_id.send_keys(email_id)

    assert email_id in driver.title


import csv

def set_up():

    driver = webdriver.chrome()

    yield driver

    driver.quite()


@pytest.fixture()
def setup():
    driver = webdriver.Chrome()

    yield driver
    import By
    driver.close()


def positive_test(setup):
    import driver
    driver.get("http:/www.test.com")

    loginbutton = driver.find_element(by=By.XPATH, value="test")
    loginbutton.click()

    email_field = driver.find_element(by=By.XPATH, value="testone")
    email_field.send_keys



user1,password1
user2,password2
user3,password3
user4,password4

pip install openpyxl

import csv

from selenium import webdriver

import pytest

driver = webdriver.Chrome()







import pytest

from selenium import webdriver

def test_one():
    driver = webdriver.chrome()


from selenium import webdriver
from selenium.webdriver.common.keys import keys
import time

driver = webdriver.Chrome(executable_path = 'path')



from selenium import webdriver

import time

driver = webdriver.Chrome(executable_path='path')

driver.get("https://www.test.com")


search_box = driver.find_element


from selenium import webdriver

import By
import time
from selenium.webdriver.common.keys import keys


from selenium.webdriver.common.keys import keys

def test_one():
    driver = webdriver.CHrome("expath")

    driver.get("https://pmapp.devpropvivo.com/login")


