from library import SeleniumWrapper
from reading_locators import read_locators

class LoginPage:

    _locators = read_locators('Login')

    def __init__(self,driver):
        self.driver =driver

    def login(self, email, password):
        sw = SeleniumWrapper(self.driver)
        # sw.enter_text(('id', 'Email'), value=email)
        # sw.enter_text(('id', 'Password'), value=password)
        # sw.click_element(('xpath', '//input[@value="Log in"]'))
        sw.enter_text(self._locators['text_email'], value=email)
        sw.enter_text(self._locators['text_paswd'], value=password)
        sw.click_element(self._locators['button_login'])

