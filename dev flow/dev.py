import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait(120)
driver.get("https://www.devpropvivo.com")
time.sleep(5)
Login_button = driver.find_element(by=By.CSS_SELECTOR,value="#propVivoLoginBtn")
Login_button.click()
time.sleep(5)
Email_box = driver.find_element(by=By.ID, value="mat-input-0")
Email_box.send_keys("vipulkadam.vk9@gmail.com")
time.sleep(5)
Password_box = driver.find_element(by=By.ID, value="mat-input-1")
Password_box.send_keys("Vipul@123")
time.sleep(5)
Login_button = driver.find_element(by=By.CSS_SELECTOR, value="body > app-root > app-login > div > div > div.col-md-6.login-form-cotainer > form > button")
Login_button.click()
time.sleep(10)
Navigation_button = driver.find_element(by=By.XPATH, value="/html/body/app-root/app-main/app-header/header/div/div/div[1]/div[1]/div")
Navigation_button.click()
time.sleep(5)
Meeting_button = driver.find_element(by=By.XPATH, value="/html/body/app-root/app-main/app-header/nav/div/div[3]/div[1]/h5/ul/li/a")
Meeting_button.click()
time.sleep(5)
Pluse_button = driver.find_element(by=By.XPATH, value="/html/body/app-root/app-main/app-pm-meeting/div/div[1]/div[2]/button/i")
Pluse_button.click()
time.sleep(5)
wait = WebDriverWait(driver, 10)
element_inside_frame = wait.until(EC.presence_of_element_located((By.ID, 'pv-meeting-add-edit')))
#element_inside_frame.click()
selectassociationdropdown = driver.find_element(by=By.XPATH, value="//input[@formcontrolname='association']")
selectassociationdropdown.click()
time.sleep(4)

#element = driver.find_element(by=By.ID, value="pv-meeting-add-edit")
#wait.until(EC.frame_to_be_available_and_switch_to_it((By.NAME, 'meeting_detail')))
#time.sleep()
