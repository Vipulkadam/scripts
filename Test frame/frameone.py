import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait(120)
driver.get("https://www.devpropvivo.com")
time.sleep(3)
Login_button = driver.find_element(by=By.CSS_SELECTOR,value="#propVivoLoginBtn")
Login_button.click()
time.sleep(3)
Email_box = driver.find_element(by=By.ID, value="mat-input-0")
Email_box.send_keys("vipulkadam.vk9@gmail.com")
time.sleep(2)
Password_box = driver.find_element(by=By.ID, value="mat-input-1")
Password_box.send_keys("Vipul@123")
time.sleep(2)
Login_button = driver.find_element(by=By.CSS_SELECTOR, value="body > app-root > app-login > div > div > div.col-md-6.login-form-cotainer > form > button")
Login_button.click()
time.sleep(10)
#navigation_button = driver.find_element(by=By.XPATH, value="/html[1]/body[1]/app-root[1]/app-main[1]/app-header[1]/header[1]/div[1]/div[1]/div[1]/div[1]/div[1]")
#navigation_button.click()
driver.maximize_window()
dropdown= driver.find_element(by=By.ID, value="mat-select-4")
select = Select(dropdown)
select.select_by_visible_text("In Progress")
#Alllist= driver.find_element(by=By.XPATH, value="//div[@role='listbox']/mat-option")

#for ALL in Alllist:
    #if ALL.text=="SNS Platina":
     #   ALL.click
      #  break

#class demodropdown():
 #   def demo_dropdown(self):
