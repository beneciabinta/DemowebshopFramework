import time
import pytest
from library import SeleniumWrapper
from homepage import HomePage
from registrationPage import RegistrationPage


from pytest import mark

headers = "gender,fname,lname,email,password"
data =[('Male','Ben','Ten','benten@c.com','asdf1234'),('Female','Beni','Sen','benisen@c.com','fdsa1234')]

@mark.parametrize(headers,data)
def test_register(_driver,gender,fname,lname,email,password):
    sw = SeleniumWrapper(_driver)
    home_obj = HomePage(_driver)
    home_obj.home_register()

    register_obj = RegistrationPage(_driver)
    register_obj.register(gender,fname,lname,email,password)
