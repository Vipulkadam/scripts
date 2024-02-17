import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait(120)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")



Username_box = driver.find_element(by=By.NAME, value="username")
Username_box.send_keys("Admin")
Password_box = driver.find_element(by=By.NAME, value="password")
Password_box.send_keys("admin123")
login_button = driver.find_element(by=By.CSS_SELECTOR, value="#app > div.orangehrm-login-layout > div > div.orangehrm-login-container > div > div.orangehrm-login-slot > div.orangehrm-login-form > form > div.oxd-form-actions.orangehrm-login-action > button")
login_button.click()
time.sleep(5)
Admin_button = driver.find_element(by=By.CSS_SELECTOR, value="#app > div.oxd-layout > div.oxd-layout-navigation > aside > nav > div.oxd-sidepanel-body > ul > li:nth-child(1) > a")
Admin_button.click()
time.sleep(5)
PIM_button = driver.find_element(by=By.CSS_SELECTOR, value= "#app > div.oxd-layout > div.oxd-layout-navigation > aside > nav > div.oxd-sidepanel-body > ul > li:nth-child(2) > a")
PIM_button.click()
time.sleep(5)
Add_button = driver.find_element(by=By.CSS_SELECTOR,value="#app > div.oxd-layout > div.oxd-layout-container > div.oxd-layout-context > div > div.orangehrm-paper-container > div.orangehrm-header-container > button")
Add_button.click()
time.sleep(5)
FirstName_box = driver.find_element(by=By.NAME, value="firstName")
FirstName_box.send_keys("TOM")
time.sleep(5)
MiddleName_box = driver.find_element(by=By.NAME, value="middleName")
MiddleName_box.send_keys("SHON")
time.sleep(5)
LastName_box = driver.find_element(by=By.NAME, value="lastName")
LastName_box.send_keys("SMITH")
time.sleep(5)
Save_button = driver.find_element(by=By.CSS_SELECTOR, value="#app > div.oxd-layout > div.oxd-layout-container > div.oxd-layout-context > div > div > form > div.oxd-form-actions > button.oxd-button.oxd-button--medium.oxd-button--secondary.orangehrm-left-space")
Save_button.click()
time.sleep(5)
Myinfo_button = driver.find_element(by=By.CSS_SELECTOR, value="#app > div.oxd-layout > div.oxd-layout-navigation > aside > nav > div.oxd-sidepanel-body > ul > li:nth-child(6) > a > span")
Myinfo_button.click()
time.sleep(5)
#Nickname_box = driver.find_element(by=By.XPATH, value="//input[@class='oxd-input oxd-input--active']")
Nickname_box = driver.find_element(by=By.CSS_SELECTOR, value="#app > div.oxd-layout > div.oxd-layout-container > div.oxd-layout-context > div > div > div > div.orangehrm-edit-employee-content > div.orangehrm-horizontal-padding.orangehrm-vertical-padding > form > div:nth-child(1) > div.oxd-grid-3.orangehrm-full-width-grid > div > div > div:nth-child(2) > input")
Nickname_box.send_keys("Smith")
time.sleep(5)
OtherId_box = driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[1]/div[2]/div/div[2]/input")
OtherId_box.send_keys("100")
time.sleep(5)


