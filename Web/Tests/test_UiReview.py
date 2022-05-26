import pytest
import allure
from Web.Base.base import Base
from Web.Pages.ReviewPage import ReviewPage


@pytest.mark.usefixtures('sing')
@allure.description("UI review page tests")
@allure.severity(severity_level="MEDIUM")
class TestReview(Base):

    def test_ui_babershop_sigh(self):
        # setup call driver ReviewPage
        driver = self.driver
        print("login successfully")
        page = ReviewPage(driver)
        # tensfer to review page
        page.click_review_page()

        value = page.Ui_barbershop_sing()
        try:
            assert value == "wondemagen barbershop"
        finally:
            if (AssertionError):
                allure.attach(driver.get_screenshot_as_png(),
                              name="sing dont match!!",attachment_type=allure.attachment_type.PNG)

    def test_ui_form_title(self):
        # setup call driver ReviewPage
        driver = self.driver
        print("login successfully")
        page = ReviewPage(driver)
        # tensfer to review page
        page.click_review_page()

        value = page.Ui_form_title()
        try:
            assert value == "User Reviews"
        finally:
            if (AssertionError):
                allure.attach(driver.get_screenshot_as_png(),
                              name="title dont match!!", attachment_type=allure.attachment_type.PNG)

    def test_ui_table_title(self):
        # setup call driver ReviewPage
        driver = self.driver
        print("login successfully")
        page = ReviewPage(driver)
        # tensfer to review page
        page.click_review_page()
        # get table text
        print("get title text")
        value = page.Ui_table_title()
        try:
            assert value == "full name	barber name	review"
        finally:
            if (AssertionError):
                allure.attach(driver.get_screenshot_as_png(),
                              name="title dont match!!", attachment_type=allure.attachment_type.PNG)






