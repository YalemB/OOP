import allure
import requests
import random
import pytest
num = random.random()
class TestApi():


    #1
    def test_register_user_correctly(self):
        url = "https://identitytoolkit.googleapis.com/v1/accounts:signUp?key=AIzaSyDlGs3dgSBMSYNCkGQnKc1cQanS0xb3GoM"
        myobj = {f"email":f"y@b{random.random()}.com",
                 "password":"123456",
                 "confirmPassword":"123456"}

        value = requests.post(url, data=myobj)
        print(myobj.values())
        print("")
        print(value.status_code)
        assert value.status_code == 200

    #2
    def test_register_with_existed_user(self):
        url = "https://identitytoolkit.googleapis.com/v1/accounts:signUp?key=AIzaSyDlGs3dgSBMSYNCkGQnKc1cQanS0xb3GoM"
        myobj = {"email":"y@b.com",
                 "password":"123456",
                 "confirmPassword":"123456"}

        value = requests.post(url, data=myobj)
        print("")
        print(value.status_code)
        assert value.status_code == 400
    #3
    def test_login_with_existed_user_correctly(self):
        url = "https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key=AIzaSyDlGs3dgSBMSYNCkGQnKc1cQanS0xb3GoM"
        myobj = {"email":"y@b.com","password":"123456"}

        value = requests.post(url, data=myobj)
        print("")
        print(value.status_code)
        assert value.status_code == 200
    #4
    def test_transfer_to_staff_page_(self):
        url = "https://wondemagen-barbershop.herokuapp.com/staff"
        value = requests.get(url)
        print("")
        print(value.status_code)
        assert value.status_code == 200
    #5
    def test_leve_comment_for_barber(self):
        url = "https://wondemagen-barbershop.herokuapp.com/user_rating"
        myobj = {"fullName":"yalem",
                 "barberName":"aviel",
                 "review":"bbb"}

        value = requests.post(url, data=myobj)
        print("")
        print(value.status_code)
        assert value.status_code == 201
    #6
    def test_leve_comment_to_admin(self):
        url = "https://wondemagen-barbershop.herokuapp.com/user_messages"
        myobj = {"fullName":"yalem",
                 "phoneNumber":"0551111111",
                 "message":"test"}

        value = requests.post(url, data=myobj)
        print("")
        print(value.status_code)
        assert value.status_code == 201


    #7

    def test_get_list_of_users(self):
        url = "https://reqres.in/api/users?page=2"

        value = requests.get(url)
        print("")
        print(value.status_code)

        assert value.status_code == 200



    #8
    def test_create_new_user(self):
        url = "https://reqres.in/api/users"
        myobj = {"name":"yalem",
                 "job":"coach"}

        value = requests.post(url, data=myobj)
        print("")
        print(value.status_code)
        assert value.status_code == 201


    #9
    def test_register_successfully(self):
        url = "https://reqres.in/api/register"
        myobj = {"email":"eve.holt@reqres.in",
                 "password":"pistol"}

        value = requests.post(url, data=myobj)
        print("")
        print(value.status_code)
        assert value.status_code == 200
    #10
    def test_register_unsuccessfully(self):
        url = "https://reqres.in/api/register"
        myobj = {"email":"eve.holt@reqres.in"}

        value = requests.post(url, data=myobj)
        print("")
        print(value.status_code)
        assert value.status_code == 400


    @allure.step("register successfully")
    def test_register_successfully(self):
        url = "https://ivolunteer-app.herokuapp.com/users/register"
        myobj = {"FirstName":"test02",
                 "LastName":"test",
                 "Email":f"test{num}@test.com",
                 "Password":"123456",
                 "Age":"27",
                 "ProfilePic":"test"}

        send = requests.post(url, json=myobj)
        value = send.json()
        print("")
        print(send.status_code)
        assert send.status_code == 200
        assert value["Message"] == "User Added Successfully"


    @allure.step("register unsuccessfully")
    def test_register_unsuccessfully_email_existed(self):
        url = "https://ivolunteer-app.herokuapp.com/users/register"
        myobj = {"FirstName":"test02",
                 "LastName":"test",
                 "Email":"test02@test.com",
                 "Password":"123456",
                 "Age":"27",
                 "ProfilePic":"test"}

        send = requests.post(url, json=myobj)
        value = send.json()
        print("")
        print(send.status_code)
        assert send.status_code == 400
        assert  send.elapsed.total_seconds() < 15
        assert value["Message"] == "~~Email Already Used~~"




















