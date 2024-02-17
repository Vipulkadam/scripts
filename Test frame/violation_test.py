from selenium import webdriver
from selenium.common import NoSuchElementException
import pytest

from pynput.keyboard import Key, Controller
from selenium.webdriver.support import wait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
@pytest.fixture()
def test_Setup():
    global driver
    import time
    global time
    from selenium.webdriver.chrome.service import Service as ChromeService
    from selenium.webdriver.common.by import By
    global By
    from webdriver_manager.chrome import ChromeDriverManager

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(20)

def test_negativevolation(test_Setup):
    driver.get("https://www.devpropvivo.com")
    try:
        emailfield = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH,
                                              '/html[1]/body[1]/div[2]/div[1]/div[3]/ul[1]/li[7]/a[1]'))
        )
        print("Loging button successfully!")
    except Exception as e:

        print("Visibility failed:", e)
    Login_button = driver.find_element(by=By.CSS_SELECTOR, value="#propVivoLoginBtn")
    Login_button.click()
    try:
        emailfield = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH,
                                              '/html[1]/body[1]/app-root[1]/app-login[1]/div[1]/div[1]/div[2]/form[1]/div[1]/mat-form-field[1]/div[1]/div[1]/div[1]/input[1]'))
        )
        print("Form submitted successfully!")
    except Exception as e:

        print("Form submission failed:", e)

    Email_box = driver.find_element(by=By.ID, value="mat-input-0")
    Email_box.send_keys("vipulkadam.vk9@gmail.com")
    time.sleep(1)
    Password_box = driver.find_element(by=By.ID, value="mat-input-1")
    Password_box.send_keys("Vipul@123")
    time.sleep(2)
    Login_button = driver.find_element(by=By.CSS_SELECTOR,
                                       value="body > app-root > app-login > div > div > div.col-md-6.login-form-cotainer > form > button")
    Login_button.click()
    time.sleep(10)
    try:
        create = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//body//app-root//header//ul//a[1]'))
        )
        print("Form submitted successfully!")
    except Exception as e:

        print("Form submission failed:", e)


    try:
        error_message = driver.find_element(By.ID, 'error_message')
        print("Error occurred:", error_message.text)
    except NoSuchElementException:
        print("No errors detected. Form submitted successfully!")
        driver.maximize_window()


