
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

#driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#driver.implicitly_wait(120)
#driver.get("https://www.devpropvivo.com")
#time.sleep(5)
#Login_button = driver.find_element(by=By.CSS_SELECTOR,value="#propVivoLoginBtn")
#Login_button.click()
#time.sleep(5)
#Email_box = driver.find_element(by=By.ID, value="mat-input-0")
#Email_box.send_keys("vipulkadam.vk9@gmail.com")
#time.sleep(5)
#Password_box = driver.find_element(by=By.ID, value="mat-input-1")
#Password_box.send_keys("Vipul@123")
#time.sleep(5)
#Login_button = driver.find_element(by=By.CSS_SELECTOR, value="body > app-root > app-login > div > div > div.col-md-6.login-form-cotainer > form > button")
#Login_button.click()
#time.sleep(10)


print("reels, star")
if 5 > 2:
    print("five is greater than two!")

    X = 5
    y = "jhon"
    print(X)
    print(y)

    x = "python"
    y = "is"
    z = "awesome"
    print(x,y,z)
    #a == b
    #a != b
    #a =< b
    #a < b
    #a > b

    a = 200
    b = 200
    if b > a:
        print("b is greater then a")
    elif a == b:
        print("a and b are equal")


i = 1
while i < 6:
    print(i)
    break



def my_function():
    print("hello from function")

my_function()








