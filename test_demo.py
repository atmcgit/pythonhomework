from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains

# prefix => ön ek test
# postfix


class Test_DemoClass:
    # her testten önce çağırılır
    def setup_method(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install)
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")

    # her testten sonra çağırılır
    def teardown_method(self):
        self.driver.quit()

    def test_demoFunc(self):
        print("demo test")
        # 3A Act Arrange Assert
        text = "Hello"
        assert text == "Hello"

    def test_demo2(self):
        assert True

    def test_invalid_login(self):
