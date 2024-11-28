from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located

def _wait(func):
    def wrapper(*args,**kwargs):
        instance,locator = args
        ws = WebDriverWait(instance.driver,10)
        ws.until(visibility_of_element_located(locator))
        print('Waiting...')
        return func(*args,**kwargs)
    return wrapper

def cls_wait(cls):
    for key,value in cls.__dict__.items():
        if callable(value) and key != "__init__":
            setattr(cls,key,_wait(value))
    return cls

@cls_wait
class SeleniumWrapper:
    def __init__(self,driver):
        self.driver = driver


    # def click_element(loc_type,loc_value):
    # def click_element(locator):
    # @_wait
    def click_element(self,locator,/):
        # loc_type,loc_value = locator
        self.driver.find_element(*locator).click()

    # def enter_text(loc_type,loc_value,value):
    # def enter_text(locator,value):
    # @_wait
    def enter_text(self,locator,/,*, value):
        loc_type, loc_value= locator
        self.driver.find_element(*locator).clear()
        self.driver.find_element(*locator).send_keys(value)

    # def select_item(locator,item):
    # @_wait
    def select_item(self,locator,/,*, item):
        element = self.driver.find_element(*locator)
        select = Select(element)
        select.select_by_visible_text(item)