from library import SeleniumWrapper
import time
from reading_locators import read_locators

from homepage import HomePage

class RegistrationPage:

    _locators = read_locators('registration')

    def __init__(self,driver):
        self.driver =driver

    def register(self, gender, fname, lname, email, password):
        sw = SeleniumWrapper(self.driver)
        # sw.click_element(('xpath', '//a[text()="Register"]'))
        # if gender.upper() == 'MALE':
        #     sw.click_element(('id', 'gender-male'))
        # elif gender.upper() == 'FEMALE':
        #     sw.click_element(('id', 'gender-female'))
        # sw.enter_text(('id', 'FirstName'), value=fname)
        # sw.enter_text(('id', 'LastName'), value=lname)
        # sw.enter_text(('name', 'Email'), value=email)
        # sw.enter_text(('name', 'Password'), value=password)
        # sw.enter_text(('name', 'ConfirmPassword'), value=password)
        # sw.click_element(('xpath', '//input[@value="Register"]'))
        # time.sleep(2)

        if gender.upper() == 'MALE':
            sw.click_element(self._locators['rdo_female'])
        elif gender.upper() == 'FEMALE':
            sw.click_element(self._locators['rdo_male'])
        sw.enter_text(self._locators['text_fname'], value=fname)
        sw.enter_text(self._locators['text_lname'], value=lname)
        sw.enter_text(self._locators['text_email'], value=email)
        sw.enter_text(self._locators['text_pswd'], value=password)
        sw.enter_text(self._locators['text_cnfmpswd'], value=password)
        sw.click_element(self._locators['button_register'])
        time.sleep(2)
