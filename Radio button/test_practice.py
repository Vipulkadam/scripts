from selenium import webdriver
from selenium.common import NoSuchElementException
global time
import time
import pytest
from pynput.keyboard import Key, Controller
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class test():
    @pytest.fixture()
    def test_setup(self):
        global driver
        from selenium.webdriver.chrome.service import Service as ChromeService
        global By
        from webdriver_manager.chrome import ChromeDriverManager
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.implicitly_wait(10)


    def test_positiveflow(test_setup):
        driver.get("https://www.devpropvivo.com")
        time.sleep(5)
        Login_button = driver.find_element(by=By.CSS_SELECTOR, value="#propVivoLoginBtn")
        Login_button.click()
        time.sleep(2)
        Email_box = driver.find_element(by=By.ID, value="mat-input-0")
        Email_box.send_keys("vipulkadam.vk9@gmail.com")