import time
from library import SeleniumWrapper
from homepage import HomePage

from loginPage import LoginPage

from pytest import mark

headers= "email,password"
data =[('benten@c.com','asdf1234'),('benisen@c.com','fdsa1234')]

@mark.parametrize(headers,
                  data)
def test_login(_driver,_config,email,password):
    # sw= SeleniumWrapper(_driver)
    home_obj = HomePage(_driver)
    home_obj.home_login()
    login_obj = LoginPage(_driver)
    login_obj.login(email,password)




