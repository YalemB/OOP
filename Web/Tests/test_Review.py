import pytest
import allure
from Web.Pages.ReviewPage import ReviewPage
from Web.Utiltis.utiles import Utiles
from Web.Base.base import Base


@pytest.mark.usefixtures('sing')
@allure.description("review page tests")
@allure.severity(severity_level="CRITICAL")
class TestReview(Base):

    #write a review for aviel
    @pytest.mark.sanity
    def test_leave_review_correctly_for_aviel(self):
        # setup call driver, utiles, and ReviewPage
        driver = self.driver
        util = Utiles()
        print("login successfully")
        page = ReviewPage(driver)
        #tensfer to review page
        page.click_review_page()
        #get the leve review form fields
        form = page.fill_form()
        # data to insert the form: barber name, username, message
        data = ["aviel", "meek mill", "dope barber"]
        expected_result = True
        # validation if the form filled correctly
        util.send_message_button(form,data,expected_result)
        # if the form filled correctly click the send button
        form[-1].click()
        # switch to alewrt to get the message of validation of leaving message correctly
        obj = driver.switch_to.alert
        text = obj.text
        obj.accept()
        try:
            assert text == "the review was sent successfully"
        finally:
            if (AssertionError):
                allure.attach(driver.get_screenshot_as_png(),
                              name="message dont match!!",attachment_type=allure.attachment_type.PNG)

    # write a review for oshre
    @pytest.mark.sanity
    def test_leave_review_correctly_for_osher(self):
        # setup call driver, utiles, and ReviewPage
        driver = self.driver
        util = Utiles()
        print("login successfully")
        page = ReviewPage(driver)
        # tensfer to review page
        page.click_review_page()
        # get the leve review form fields
        form = page.fill_form()
        # data to insert the form: barber name, username, message
        data = ["osher", "lil", "very professional"]
        expected_result = True
        # validation if the form filled correctly
        util.send_message_button(form, data, expected_result)
        # if the form filled correctly click the send button
        form[-1].click()
        # switch to alewrt to get the message of validation of leaving message correctly
        obj = driver.switch_to.alert
        text = obj.text
        obj.accept()

        try:
            assert text == "the review was sent successfully"
        finally:
            if (AssertionError):
                allure.attach(driver.get_screenshot_as_png(),
                              name="message dont match!!",attachment_type=allure.attachment_type.PNG)


    def test_validate_reivew_message_for_aviel(self):
        # setup call driver, and ReviewPage
        driver = self.driver
        print("login successfully")
        page = ReviewPage(driver)
        page.click_review_page()
        # comment = the message that was sent in the previous test----->test_leave_review_correctly_for_aviel
        comment = page.valdait_commet_aviel()

        try:
            assert comment.text == "dope barber"
        finally:
            if (AssertionError):
                allure.attach(driver.get_screenshot_as_png(),
                              name="commets dont match!!",attachment_type=allure.attachment_type.PNG)


    def test_validate_reivew_message_for_osher(self):
        # setup call driver, and ReviewPage
        driver = self.driver
        print("login successfully")
        page = ReviewPage(driver)
        page.click_review_page()
        # comment = the message that was sent in the previous test----->test_leave_review_correctly_for_aviel
        comment = page.valdait_comme_osher()

        try:
            assert comment.text == "Good barber"
        finally:
            if (AssertionError):
                allure.attach(driver.get_screenshot_as_png(),
                              name="commets dont match!!",attachment_type=allure.attachment_type.PNG)



    def test_leave_review_incorrectly_by_diff_barber(self):
        # setup call driver, utiles, and ReviewPage
        driver = self.driver
        util = Utiles()
        print("login successfully")
        page = ReviewPage(driver)
        page.click_review_page()
        form = page.fill_form()
        # data to insert the form: barber name, username, message
        data = ["mosha", "yalem", " Not Good barber"]
        expected_result = False

        util.send_message_button(form, data, expected_result)


    #barber name field null
    @pytest.mark.skip
    def test_leave_review_incorrectly_by_null_barber_name(self):
        # setup call driver, utiles, and ReviewPage
        driver = self.driver
        util = Utiles()
        print("login successfully")
        page = ReviewPage(driver)
        page.click_review_page()
        form = page.fill_form()
        # data to insert the form: barber name, username, message
        data = ["", "yalem", " Not Good barber"]
        expected_result = False

        util.send_message_button(form, data, expected_result)

    # barber name field null
    @pytest.mark.skip
    def test_leave_review_incorrectly_by_null_full_name(self):
        # setup call driver, utiles, and ReviewPage
        driver = self.driver
        util = Utiles()
        print("login successfully")
        page = ReviewPage(driver)
        page.click_review_page()
        form = page.fill_form()
        # data to insert the form: barber name, username, message
        data = ["aviel", "", " Not Good barber"]
        expected_result = False

        util.send_message_button(form, data, expected_result)

    # barber message_field null
    def test_leave_review_incorrectly_by_null_message_field(self):
        # setup call driver, utiles, and ReviewPage
        driver = self.driver
        util = Utiles()
        print("login successfully")
        page = ReviewPage(driver)
        page.click_review_page()
        form = page.fill_form()
        # data to insert the form: barber name, username, message
        data = ["aviel", "yalem", ""]
        expected_result = False

        util.send_message_button(form, data, expected_result)

    #only message field
    def test_leave_review_incorrectly_by_only_message_field(self):
        # setup call driver, utiles, and ReviewPage
        driver = self.driver
        util = Utiles()
        print("login successfully")
        page = ReviewPage(driver)
        page.click_review_page()
        form = page.fill_form()
        # data to insert the form: barber name, username, message
        data = ["", "", " Not Good barber"]
        expected_result = False

        util.send_message_button(form, data, expected_result)

    # only fullname field
    def test_leave_review_incorrectly_by_only_fullname(self):
        # setup call driver, utiles, and ReviewPage
        driver = self.driver
        util = Utiles()
        print("login successfully")
        page = ReviewPage(driver)
        page.click_review_page()
        form = page.fill_form()
        # data to insert the form: barber name, username, message
        data = ["", "yalem", ""]
        expected_result = False

        util.send_message_button(form, data, expected_result)

    # all fields null
    @pytest.mark.sanity
    def test_leave_review_incorrectly_by_null_all_field(self):
         # setup call driver, utiles, and ReviewPage
         driver = self.driver
         util = Utiles()
         print("login successfully")
         page = ReviewPage(driver)
         page.click_review_page()
         form = page.fill_form()
         # data to insert the form: barber name, username, message
         data = ["", "", ""]
         expected_result = False

         util.send_message_button(form, data, expected_result)
