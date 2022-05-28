import allure
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from Web.Locators.LoginLocators import LoginLocators



class LoginPage():
    def __init__(self,driver:WebDriver):
        self.driver = driver
        self.log_btn_name = LoginLocators.log_btn_name
        self.email_txtbox_name = LoginLocators.email_txtbox_name
        self.pass_txtbox_name = LoginLocators.pass_txtbox_name
        self.login_btn_name = LoginLocators.login_btn_name
        self.logout_btn_name = LoginLocators.logout_btn_name
        self.incorrect_message = LoginLocators.incorrect_message

    @allure.step("click log button")
    def click_log(self):
        self.driver.find_element(By.XPATH, self.log_btn_name).click()

    @allure.step("enter email")
    def enter_email(self, email):
        self.driver.find_element(By.XPATH, self.email_txtbox_name).clear()
        self.driver.find_element(By.XPATH, self.email_txtbox_name).send_keys(email)

    @allure.step("enter password")
    def enter_password(self, password):
        self.driver.find_element(By.XPATH, self.pass_txtbox_name).clear()
        self.driver.find_element(By.XPATH, self.pass_txtbox_name).send_keys(password)

    @allure.step("click login button")
    def click_login(self):
        return self.driver.find_element(By.XPATH, self.login_btn_name)

    @allure.step("click logout button")
    def logout_btn(self):
        return self.driver.find_element(By.XPATH, self.logout_btn_name)

    @allure.step("get alert message")
    def message_alert(self):
        return self.driver.find_element(By.XPATH, self.incorrect_message)

    @allure.step("get alert message")
    def message_error(self):
        return self.driver.find_element(By.XPATH, self.email_txtbox_name).get_attribute("validationMessage")

