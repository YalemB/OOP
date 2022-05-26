import pytest
import allure
from Web.Pages.LoginPage import LoginPage
from Web.Base.base import Base


@pytest.mark.usefixtures('set_up')
@allure.description("Login page tests")
@allure.severity(severity_level="CRITICAL")
class TestLogin(Base):
    @pytest.mark.sanity
    def test_login_correctly(self):
        # setup call driver and LoginPage
        driver = self.driver
        login = LoginPage(driver)
        login.click_log()
        #insert data
        login.enter_email("b@k.com")
        login.enter_password("123456")
        login.click_login().click()

        value = login.logout_btn().text

        assert value == "log out"

    @pytest.mark.sanity
    def test_invalid_login_when_email_incorrect(self):
        # setup call driver and LoginPage
        driver = self.driver
        login = LoginPage(driver)
        login.click_log()
        # insert data
        login.enter_email("bom@.")
        login.enter_password("123456")
        login.click_login()

        value = login.message_error()
        print(value)

        assert value != ""

    @pytest.mark.sanity
    def test_invalid_login_when_password_incorrect(self):
        # setup call driver and LoginPage
        driver = self.driver
        login = LoginPage(driver)
        login.click_log()
        # insert data
        login.enter_email("b@k.com")
        login.enter_password("111111")
        login.click_login().click()

        value = login.message_alert().text


        assert value == "incorrect Password/Email"

    @pytest.mark.skip
    def test_invalid_login_when_passwordField_is_null(self):
        # setup call driver and LoginPage
        driver = self.driver
        login = LoginPage(driver)
        login.click_log()
        # insert data
        login.enter_email("b@k.com")
        login.enter_password("")
        login.click_login()
        value = login.click_login().is_enabled()
        # button dont need to be enabled
        expected_result = False

        assert value == expected_result

    @pytest.mark.skip
    def test_invalid_login_when_emailField_is_null(self):
        # setup call driver and LoginPage
        driver = self.driver
        login = LoginPage(driver)
        login.click_log()
        # insert data
        login.enter_email("")
        login.enter_password("123456")
        login.click_login()
        value = login.click_login().is_enabled()
        # button dont need to be enabled
        expected_result = False

        assert value ==expected_result

    @pytest.mark.sanity
    def test_invalid_login_when_all_fields_are_null(self):
        # setup call driver and LoginPage
        driver = self.driver
        login = LoginPage(driver)
        login.click_log()
        # insert data
        login.enter_email("")
        login.enter_password("")
        login.click_login()
        value = login.click_login().is_enabled()
        #button dont need to be enabled
        expected_result = False

        assert value == expected_result


