

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.chrome.service import Service as ChromeService


from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
def test_login_flow():

    driver.get("https://www.devpropvivo.com/")
    driver.implicitly_wait(10)
    login_button = driver.find_element(by=By.ID, value ="propVivoLoginBtn")

    login_button.click()

    Email_field = driver.find_element(by=By.ID, value = "mat-input-0")
    Email_field.send_keys("vipulkadam.vk9@gmail.com")

    time.sleep(3)

    Passwod_field = driver.find_element(by=By.ID, value = "mat-input-1")
    Passwod_field.send_keys("Vipul@12")

    login_one_button = driver.find_element(by=By.CSS_SELECTOR, value ="btn btn-blue form-control")
    login_one_button.click()

    time.slip(10)



