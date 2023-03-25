from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By


class Test:

    def empty_user_password(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        usernameInput = driver.find_element(By.ID, "user-name")
        passwordInput = driver.find_element(By.ID, "password")
        loginBtn = driver.find_element(By.ID, "login-button")
        usernameInput.send_keys("")
        passwordInput.send_keys("")
        loginBtn.click()
        sleep(5)
        errorMessage = self.driver.find_element(
            By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Username is required"
        print(testResult)

    def only_password_empty(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        usernameInput = driver.find_element(By.ID, "user-name")
        passwordInput = driver.find_element(By.ID, "password")
        loginBtn = driver.find_element(By.ID, "login-button")
        usernameInput.send_keys("standard_user")
        passwordInput.send_keys("")
        loginBtn.click()
        sleep(5)
        errorMessage = self.driver.find_element(
            By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Password is required"
        print(testResult)

    def locked_user(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        usernameInput = driver.find_element(By.ID, "user-name")
        passwordInput = driver.find_element(By.ID, "password")
        loginBtn = driver.find_element(By.ID, "login-button")
        usernameInput.send_keys("locked_out_user")
        passwordInput.send_keys("secret_sauce")
        loginBtn.click()
        sleep(5)
        errorMessage = self.driver.find_element(
            By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Sorry, this user has been locked out."
        print(testResult)

    def x_button(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        loginBtn = driver.find_element(By.ID, "login-button")
        loginBtn.click()
        sleep(5)
        error1 = driver.find_element(
            By.CSS_SELECTOR, "#login_button_container > div > form > div:nth-child(1) > svg")
        userErrorVarMi = error1.is_displayed()
        print(userErrorVarMi)
        sleep(5)
        error2 = driver.find_element(
            By.CSS_SELECTOR, "#login_button_container > div > form > div:nth-child(2) > svg")
        passwordErrorVarMi = error2.is_displayed()
        print(passwordErrorVarMi)
        sleep(5)
        errorClose = driver.find_element(By.CLASS_NAME, "error-button")
        errorClose.click()
        sleep(5)

    def go_ınventory(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        usernameInput = driver.find_element(By.ID, "user-name")
        passwordInput = driver.find_element(By.ID, "password")
        loginBtn = driver.find_element(By.ID, "login-button")
        usernameInput.send_keys("standard_user")
        passwordInput.send_keys("secret_sauce")
        loginBtn.click()
        sleep(2)
        currentUrl = driver.current_url == "https://www.saucedemo.com/inventory.html"
        print(currentUrl)

    def count_product(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        usernameInput = driver.find_element(By.ID, "user-name")
        passwordInput = driver.find_element(By.ID, "password")
        loginBtn = driver.find_element(By.ID, "login-button")
        usernameInput.send_keys("standard_user")
        passwordInput.send_keys("secret_sauce")
        loginBtn.click()
        sleep(2)
        product = driver.find_elements(By.CLASS_NAME, "inventory_item")
        print(len(product))
        number = len(product) == 6
        print(number)


testclass = Test()
testclass.count_product()
