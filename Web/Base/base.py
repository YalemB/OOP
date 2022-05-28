import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from Web.Pages.LoginPage import LoginPage




class Base():

    @pytest.fixture(autouse=True)
    def set_up(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        # self.driver = webdriver.Chrome("..\Drivers\chromedriver.exe")

        self.driver.implicitly_wait(10)
        self.driver.get("https://wondemagen-barbershop.herokuapp.com")
        self.driver.maximize_window()
        yield self.driver
        if self.driver is not None:
            print("-----------------------------------------")
            print("Tests is finished")
            self.driver.close()
            self.driver.quit()

    @pytest.fixture
    def sing(self):
        driver = self.driver
        email = "tsiona@gmail.com"
        password = "123456"
        login = LoginPage(driver)
        login.click_log()
        login.enter_email(email)
        login.enter_password(password)
        login.click_login().click()
        yield self.driver











