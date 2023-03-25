from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By

class Test_Sauce:
    def test_invalid_login(self):
        driver = webdriver.Chrome("C:\chromedriver.exe")
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(2)
        # en fazla 5 saniye olacak şekilde user-name id'li elemntin görünmesini bekle
        usernameInput = driver.find_element(By.ID,"user-name")
        passwordInput = driver.find_element(By.ID,"password")
        sleep(1)
        usernameInput.send_keys("1")
        passwordInput.send_keys("1")
        sleep(1)
        loginBtn = driver.find_element(By.ID,"login-button")
        loginBtn.click()
        errorMessage = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Username and password do not match any user in this service"
        print(f"TEST SONUCU : {testResult}")
        sleep(5)
     

testClass = Test_Sauce()
testClass.test_invalid_login()
sleep(2)