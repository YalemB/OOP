import allure

from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver


from Web.Locators.ReviewLocators import ReviewLocators

class ReviewPage():
    def __init__(self,driver:WebDriver):
        self.driver = driver
        self.review_page = ReviewLocators.review_page
        self.from_leve_review = ReviewLocators.from_leve_review
        self.review_comment_aviel = ReviewLocators.review_comment_aviel
        self.review_comment_osher = ReviewLocators.review_comment_osher
        self.barbershop_sing = ReviewLocators.barbershop_sing
        self.form_title = ReviewLocators.form_title
        self.table_title = ReviewLocators.table_title

    @allure.step("click review page")
    def click_review_page(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.review_page))
        ).click()

    @allure.step("get form fields")
    def fill_form(self):
        return  WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, self.from_leve_review))
        )

    @allure.step("get the comment for aviel of the user from the table")
    def valdait_commet_aviel(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.review_comment_aviel))
        )

    @allure.step("get the comment fot osher of the user from the table")
    def valdait_comme_osher(self):
        return  WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.review_comment_osher))
        )

    @allure.step("get the barbershop sing title text")
    def Ui_barbershop_sing(self):
        return self.driver.find_element(By.XPATH, self.barbershop_sing).get_attribute("innerText")

    @allure.step("get the form title text")
    def Ui_form_title(self):
        return self.driver.find_element(By.XPATH, self.form_title).get_attribute("innerText")

    @allure.step("get the table title text")
    def Ui_table_title(self):
        return self.driver.find_element(By.XPATH, self.table_title).get_attribute("innerText")








