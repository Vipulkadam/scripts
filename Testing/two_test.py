from selenium import webdriver
global time
import time
import pytest
from selenium.webdriver.common.by import By


from selenium.webdriver.common.by import By
from pynput.keyboard import Key, Controller

@pytest.fixture()
def test_setup():
    global driver
    import time

    from selenium.webdriver import ActionChains
    from selenium.webdriver.chrome.service import Service as ChromeService
    from selenium.webdriver.common.by import By
    global By
    from webdriver_manager.chrome import ChromeDriverManager

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
def test_pvscannegative(test_setup):
    driver.get("https://www.devpropvivo.com")
    time.sleep(3)
    Login_button = driver.find_element(by=By.CSS_SELECTOR, value="#propVivoLoginBtn")
    Login_button.click()
    time.sleep(4)
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
    driver.maximize_window()
    target_element = driver.find_element(by=By.XPATH,
                                         value="//a[@href='/association/accounts/budget']//span")
    driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center', inline: 'center' });",
                          target_element)
    adminutility = driver.find_element(by=By.XPATH, value="//div[14]//div[1]//h5[1]//button[1]//span[1]")
    adminutility.click()
    target_elementone = driver.find_element(by=By.XPATH, value="//a[normalize-space()='Bounce Mail']")
    driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center', inline: 'center' });",
                          target_elementone)
    time.sleep(1)
    pvscan = driver.find_element(by=By.XPATH, value="//a[normalize-space()='PV Scan']")
    pvscan.click()
    time.sleep(5)
    uploaddocument = driver.find_element(by=By.XPATH, value="//button[@mattooltip='Upload Document']//i")
    uploaddocument.click()
    time.sleep(1)
    driver.find_element(by=By.XPATH, value="//div[@id='pv-create-sidebar']")

    # selectassociation= driver.find_element(by=By.XPATH, value="//input[@formcontrolname='Association']")
    # selectassociation.click()
    # time.sleep(1)
    # options=driver.find_element(by=By.XPATH, value="/html/body/div[5]/div/div/div/mat-option[5]/span/span")
    # options.click()
    element = driver.find_element(by=By.XPATH, value="//body//app-root//div[@id='associationId']//div//div[1]//div[1]")
    element.click()
    time.sleep(1)
    dropdown_option = driver.find_element(by=By.XPATH, value="/html/body/div[5]/div/div")

    time.sleep(5)
    # print(len(associationlist))
    option_to_select = dropdown_option.find_element(By.XPATH,
                                                    '//*[contains(text(), "Cascade Crest At Lake Stevens Condominium Owners Association")]')
    option_to_select.click()
    time.sleep(2)

    time.sleep(1)
    selectvendor = driver.find_element(by=By.XPATH, value="//input[@formcontrolname='Vendor']")
    selectvendor.send_keys("Sansa")
    time.sleep(5)
    vendorname = driver.find_element(by=By.XPATH,
                                     value="//body/div/div[@dir='ltr']/div/div[@role='listbox']/mat-option[@role='option']/span[1]")
    vendorname.click()
    time.sleep(2)

    uploadbutton = driver.find_element(by=By.XPATH,
                                       value="//body/app-root/app-main/app-pv-scan/div/app-pv-scan-list/app-common-ax-integration-sidebar/div/div/app-upload-document/div/form[@name='frmProcessDocument']/div/button[1]")
    uploadbutton.click()
    time.sleep(4)

def test_pvscanpositive(test_setup):
    driver.get("https://www.devpropvivo.com")
    time.sleep(3)
    Login_button = driver.find_element(by=By.CSS_SELECTOR, value="#propVivoLoginBtn")
    Login_button.click()
    time.sleep(4)
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
    driver.maximize_window()
    target_element = driver.find_element(by=By.XPATH,
                                         value="//a[@href='/association/accounts/budget']//span")
    driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center', inline: 'center' });",
                          target_element)
    adminutility =driver.find_element(by=By.XPATH, value="//div[14]//div[1]//h5[1]//button[1]//span[1]")
    adminutility.click()
    target_elementone= driver.find_element(by=By.XPATH, value="//a[normalize-space()='Bounce Mail']")
    driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center', inline: 'center' });",
                          target_elementone)
    time.sleep(1)
    pvscan=driver.find_element(by=By.XPATH, value="//a[normalize-space()='PV Scan']")
    pvscan.click()
    time.sleep(5)
    uploaddocument= driver.find_element(by=By.XPATH, value="//button[@mattooltip='Upload Document']//i")
    uploaddocument.click()
    time.sleep(1)
    driver.find_element(by=By.XPATH, value="//div[@id='pv-create-sidebar']")

    # selectassociation= driver.find_element(by=By.XPATH, value="//input[@formcontrolname='Association']")
    # selectassociation.click()
    # time.sleep(1)
    # options=driver.find_element(by=By.XPATH, value="/html/body/div[5]/div/div/div/mat-option[5]/span/span")
    # options.click()
    element = driver.find_element(by=By.XPATH, value="//body//app-root//div[@id='associationId']//div//div[1]//div[1]")
    element.click()
    time.sleep(1)
    dropdown_option = driver.find_element(by=By.XPATH, value="/html/body/div[5]/div/div")

    time.sleep(5)
    # print(len(associationlist))
    option_to_select = dropdown_option.find_element(By.XPATH, '//*[contains(text(), "Cascade Crest At Lake Stevens Condominium Owners Association")]')
    option_to_select.click()
    time.sleep(2)

    time.sleep(1)
    selectvendor=driver.find_element(by=By.XPATH, value="//input[@formcontrolname='Vendor']")
    selectvendor.send_keys("Sansa")
    time.sleep(5)
    vendorname=driver.find_element(by=By.XPATH, value="//body/div/div[@dir='ltr']/div/div[@role='listbox']/mat-option[@role='option']/span[1]")
    vendorname.click()
    time.sleep(2)

    file_input = driver.find_element(by=By.XPATH,
                                     value="/html[1]/body[1]/app-root[1]/app-main[1]/app-pv-scan[1]/div[1]/app-pv-scan-list[1]/app-common-ax-integration-sidebar[1]/div[1]/div[2]/app-upload-document[1]/div[2]/form[1]/div[4]/div[1]/button[1]/span[1]")
    file_input.click()
    time.sleep(5)
    keyboard = Controller()
    keyboard.type("C:\\Users\\HP\\Downloads\\invoice.pdf")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(3)

    uploadbutton=driver.find_element(by=By.XPATH, value="//body/app-root/app-main/app-pv-scan/div/app-pv-scan-list/app-common-ax-integration-sidebar/div/div/app-upload-document/div/form[@name='frmProcessDocument']/div/button[1]")
    uploadbutton.click()
    time.sleep(2)
    processdocument= driver.find_element(by=By.XPATH, value="//a[normalize-space()='Process Document']")
    processdocument.click()
    time.sleep(5)
    process_button= driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[2]/div[1]/div[2]/a[1]/mat-icon[1]")
    process_button.click()
    time.sleep(7)














