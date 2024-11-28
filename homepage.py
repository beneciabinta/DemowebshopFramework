from library import SeleniumWrapper
from reading_locators import read_locators

class HomePage:

    _locators = read_locators('homepage')

    def __init__(self,driver):
        self.driver = driver

    def home_login(self):
        sw = SeleniumWrapper(self.driver)
        # sw.click_element(('link text','Log in'))
        sw.click_element(self._locators['link_register'])


    def home_register(self):
        sw =SeleniumWrapper(self.driver)
        sw.click_element(self._locators['link_login'])
