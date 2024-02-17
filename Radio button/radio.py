import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait(120)
driver.get("https://www.devpropvivo.com")
time.sleep(3)
Login_button = driver.find_element(by=By.CSS_SELECTOR,value="#propVivoLoginBtn")
Login_button.click()
time.sleep(5)
Email_box = driver.find_element(by=By.ID, value="mat-input-0")
Email_box.send_keys("vipulkadam.vk9@gmail.com")
time.sleep(2)
Password_box = driver.find_element(by=By.ID, value="mat-input-1")
Password_box.send_keys("Vipul@123")
time.sleep(2)
Login_button = driver.find_element(by=By.CSS_SELECTOR, value="body > app-root > app-login > div > div > div.col-md-6.login-form-cotainer > form > button")
Login_button.click()
time.sleep(7)
#navigation_button = driver.find_element(by=By.XPATH, value="/html[1]/body[1]/app-root[1]/app-main[1]/app-header[1]/header[1]/div[1]/div[1]/div[1]/div[1]/div[1]")
#navigation_button.click()
driver.maximize_window()
Manageassociation_dropdown =driver.find_element(by=By.XPATH, value="/html[1]/body[1]/app-root[1]/app-main[1]/app-header[1]/nav[1]/div[1]/div[7]/div[1]/h5[1]/button[1]")
Manageassociation_dropdown.click()
time.sleep(3)
poll_button = driver.find_element(by=By.XPATH, value="//a[normalize-space()='Poll']")
poll_button.click()
time.sleep(3)
addpoll_button= driver.find_element(by=By.XPATH, value="//button[@mattooltip='Add Poll']")
addpoll_button.click()
time.sleep(2)
frame = driver.find_element(by=By.XPATH, value="/html/body/app-root/app-main/app-poll-v1/app-add-edit-poll-v1/div/div/div[2]/app-poll-form/form")
time.sleep(2)
Selectassociation_dropdown =driver.find_element(by=By.XPATH, value="//input[@formcontrolname='AssociationId']")
Selectassociation_dropdown.click()
pleaseselectassociationlist =driver.find_element(by=By.XPATH, value="//body/div/div[@dir='ltr']/div/div[@role='listbox']/mat-option[17]/span[1]")
pleaseselectassociationlist.click()
time.sleep(2)
Question =driver.find_element(by=By.XPATH, value="//input[@formcontrolname='Question']")
Question.send_keys("Testpollforscriptwrritting")
time.sleep(2)
Description =driver.find_element(by=By.XPATH, value="//div[@title='Rich Text Editor, editor1']")
Description.send_keys("Testpoll")
time.sleep(2)
Option1 =driver.find_element(by=By.XPATH, value="//div[4]//div[1]//mat-form-field[1]//div[1]//div[1]//div[1]//input[1]")
Option1.send_keys("Yes")
time.sleep(2)
Option2 =driver.find_element(by=By.XPATH, value="//div[5]//div[1]//mat-form-field[1]//div[1]//div[1]//div[1]//input[1]")
Option2.send_keys("NO")
Datetimepicker =driver.find_element(by=By.XPATH, value="//*[name()='path' and contains(@d,'M15,13H16.')]")
Datetimepicker.click()
time.sleep(2)
date =driver.find_element(by=By.XPATH, value="//td[@aria-label='November 30, 2023']//div[@aria-selected='false']")
date.click()
time.sleep(3)
picker =driver.find_element(by=By.XPATH,value="/html/body/div[5]/div[2]/div/mat-datetimepicker-content/mat-datetimepicker-calendar/div[2]/mat-datetimepicker-clock/div/div[3]/div[8]")
picker.click()
time.sleep(3)
timemin =driver.find_element(by=By.XPATH, value="/html/body/div[5]/div[2]/div/mat-datetimepicker-content/mat-datetimepicker-calendar/div[2]/mat-datetimepicker-clock/div/div[4]/div[10]")
timemin.click()
time.sleep(2)
Publish_button =driver.find_element(by=By.CSS_SELECTOR, value="body > app-root > app-main > app-poll-v1 > app-add-edit-poll-v1 > div > div > div.add-edit-poll-v1__container > app-poll-form > form > div:nth-child(2) > div.col-md-12 > div > button:nth-child(3)")
Publish_button.click()
time.sleep(3)


#Customertype_dropdown = driver.find_element(by=By.XPATH, value="//body/app-root/app-main/app-pm-service-request-list/div/div/form[@name='addRequestForm']/div/mat-form-field/div/div/div/mat-select[@placeholder='Customer Type']/div/div[1]")
#Customertype_dropdown.click()
#Isathorized_radiobutton = driver.find_element(by=By.XPATH, value="//body/app-root/app-main/app-pm-service-request-list/div/div/form[@name='addRequestForm']/div/mat-radio-group[@role='radiogroup']/mat-radio-button[@value='No']/label[@for='mat-radio-3-input']/span[1]/span[1]")
#Isathorized_radiobutton.click()



#/html/body/app-root/app-main/app-pm-service-request-list/div[3]


