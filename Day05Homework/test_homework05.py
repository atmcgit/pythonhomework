from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import pytest
from pathlib import Path
from datetime import date


class Test_Homework:
    def setup_method(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")
        self.folderPath = str(date.today())
        Path(self.folderPath).mkdir(exist_ok=True)

    def teardown_method(self):
        self.driver.quit()

    def login_action(self, username, password):

        self.waitForElementVisible((By.ID, "user-name"))
        usernameInput = self.driver.find_element(By.ID, "user-name")

        self.waitForElementVisible((By.ID, "password"))
        passwordInput = self.driver.find_element(By.ID, "password")

        self.waitForElementVisible((By.ID, "login-button"))
        loginButton = self.driver.find_element(By.ID, "login-button")
        action = ActionChains(self.driver)
        action.send_keys_to_element(usernameInput, username)
        action.send_keys_to_element(passwordInput, password)
        action.click(loginButton)
        action.perform()
        # usernameInput.send_keys(username)
        # passwordInput.send_keys(password)

        # loginButton.click()
    def secreen_shot(self, testname, username, password):
        self.driver.save_screenshot(
            f"{self.folderPath}/{testname}-{username}-{password}.png")

    @pytest.mark.parametrize("username,password", [("", "")])
    def test_empty_username_password(self, username, password):
        self.login_action(username, password)
        # self.login_method("","")
        errorMessage = self.driver.find_element(
            By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        self.secreen_shot("login_action", username, password)
        assert errorMessage.text == "Epic sadface: Username is required"

    @pytest.mark.parametrize("username,password", [("standard_user", "")])
    def test_only_password_empty(self, username, password):
        self.login_action(username, password)
        errorMessage = self.driver.find_element(
            By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        self.secreen_shot("test_only_password_empty", username, password)
        assert errorMessage.text == "Epic sadface: Password is required"

    @pytest.mark.parametrize("username,password", [("mustafa", "123"), ("atmaca", "321"), ("kullaniciadi", "543")])
    def test_invalid_login(self, username, password):
        self.login_action(username, password)
        errorMessage = self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        self.secreen_shot("test_invalid_login", username, password)
        assert errorMessage.text == "Epic sadface: Username and password do not match any user in this service"

    @pytest.mark.parametrize("username,password", [("locked_out_user", "secret_sauce")])
    def test_locked_user(self, username, password):
        self.login_action(username, password)
        errorMessage = self.driver.find_element(
            By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        self.secreen_shot("test_locked_user", username, password)
        assert errorMessage.text == "Epic sadface: Sorry, this user has been locked out."

    @pytest.mark.parametrize("username,password", [("", "")])
    def test_x_button(self, username, password):
        self.login_action(username, password)
        xbutton1 = self.driver.find_element(
            By.CSS_SELECTOR, "#login_button_container > div > form > div:nth-child(1) > svg")
        xbutton2 = self.driver.find_element(
            By.CSS_SELECTOR, "#login_button_container > div > form > div:nth-child(2) > svg")
        self.secreen_shot("test_x_button", username, password)
        assert xbutton1.is_displayed() and xbutton2.is_displayed()

    @pytest.mark.parametrize("username,password", [("standard_user", "secret_sauce")])
    def test_go_inventory(self, username, password):
        self.login_action(username, password)
        self.secreen_shot("test_go_inventory", username, password)
        assert self.driver.current_url == "https://www.saucedemo.com/inventory.html"

    @pytest.mark.parametrize("username,password", [("standard_user", "secret_sauce")])
    def test_count_product(self, username, password):
        self.login_action(username, password)
        product = self.driver.find_elements(By.CLASS_NAME, "inventory_item")
        self.secreen_shot("test_count_product", username, password)
        assert len(product) == 6

    @pytest.mark.parametrize("username,password", [("standard_user", "secret_sauce")])
    def test_ordered_product_comprarison(self, username, password):
        self.login_action(username, password)
        self.waitForElementVisible((
            By.CSS_SELECTOR, "#item_4_title_link > div"))  # ürünün açılmasını bekle
        productName = self.driver.find_element(
            By.CSS_SELECTOR, "#item_4_title_link > div").text
        addToCartBtn = self.driver.find_element(
            By.ID, "add-to-cart-sauce-labs-backpack")
        addToCartBtn.click()                              # kartı siparişe ekle
        ordersBtn = self.driver.find_element(
            By.XPATH, "/html/body/div/div/div/div[1]/div[1]/div[3]/a")
        ordersBtn.click()                                 # sepete tıkla
        self.waitForElementVisible((
            By.XPATH, "//*[@id='item_4_title_link']/div"))
        orderedProductName = self.driver.find_element(
            By.XPATH, "//*[@id='item_4_title_link']/div").text
        self.secreen_shot("test_ordered_product_comprarison",
                          username, password)
        assert productName == orderedProductName

    # @pytest.mark.parametrize("username,password", [("standard_user", "secret_sauce")])
    # filtreleme düzgün çalışıyor mu ?
    def test_price_filter(self):
        self.login_action("standard_user", "secret_sauce")
        priceList = []
        self.waitForElementVisible((By.CLASS_NAME, "inventory_item_price"))
        prices = self.driver.find_elements(
            By.CLASS_NAME, "inventory_item_price")
        for i in prices:
            price = i.text.removeprefix("$")
            price = float(price)
            priceList.append(price)
        priceList.sort()
        filterLowHigh = self.driver.find_element(
            By.XPATH, "/html/body/div/div/div/div[1]/div[2]/div/span/select/option[3]")
        filterLowHigh.click()
        sortedPriceList = []
        newPrice = self.driver.find_elements(
            By.CLASS_NAME, "inventory_item_price")
        for i in newPrice:
            price = i.text.removeprefix("$")
            price = float(price)
            sortedPriceList.append(price)
        self.secreen_shot("test_price_filter", "standard_user", "secret_sauce")
        assert sortedPriceList == priceList

    def test_shopping_cart_badge(self):
        self.login_action("standard_user", "secret_sauce")
        addBackpack = self.driver.find_element(
            By.ID, "add-to-cart-sauce-labs-backpack")
        addBackpack.click()
        badge = self.driver.find_element(
            By.CLASS_NAME, "shopping_cart_badge").text
        badge = int(badge)
        addTshirt = self.driver.find_element(
            By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
        addTshirt.click()
        badge2 = self.driver.find_element(
            By.CLASS_NAME, "shopping_cart_badge").text
        badge2 = int(badge2)
        self.secreen_shot("test_shopping_cart_badge",
                          "standard_user", "secret_sauce")
        assert badge+1 == badge2

    def waitForElementVisible(self, locator, timeout=5):
        WebDriverWait(self.driver, timeout).until(
            ec.visibility_of_all_elements_located(locator))
