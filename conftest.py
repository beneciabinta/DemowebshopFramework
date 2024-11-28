import pytest
from selenium.webdriver.chrome.webdriver import WebDriver as Chrome
from selenium.webdriver.safari.webdriver import WebDriver as Safari
from selenium.webdriver.edge.webdriver import WebDriver as Edge
from selenium.webdriver.firefox.webdriver import WebDriver as Firefox

# env ='stage'
# browser_name ='firefox'

#instead of giving the above two global variables, we can use 'pytest_addoption' func to read data which are passed in the command line.
#b4 executing the test methods , pytest will search for hook functions. If any hookfunctions are found, then pytest will execute the hook func
#first and then will execute the test method
# parser is a builtin fixture
def pytest_addoption(parser):
    parser.addoption("--browser", action = "store",dest = "browser_name", default = "chrome")
    parser.addoption("--env",action = "store", dest = "env_opt",default = "test")
    parser.addoption("--timeout",action = "store", dest = "max_timeout", default = 10)

class TestConfigurations:
    url ='https://demowebshop.tricentis.com/'
    email = 'benten@c.com'
    password ='asdf1234'
    agent_id =12345

class StageConfigurations:
    url = "https://demowebshop.tricentis.com/"
    email = "bill.gates@company.com"
    password = "Password123"
    agent_id = 89989

# @pytest.fixture()
# def browser():
#     if browser_name.upper() == 'CHROME':
#         return Chrome
#     elif browser_name.upper() == 'SAFARI':
#         return Safari
#     elif browser_name.upper() == 'EDGE':
#         return Edge
#     elif browser_name.upper() == 'FIREFOX':
#         return Firefox

#request is a a built in fixture. It is used ton access the arguments in the command line as the argument
#in another fixture

@pytest.fixture()
def _config(request):
    if request.config.option.env_opt.upper() == 'TEST':
        print('Test Environment')
        return TestConfigurations
    elif request.config.option.env_opt.upper() == 'STAGE':
        print('Stage Environment')
        return StageConfigurations
    else:
        raise Exception("Unknown Environment")

# @pytest.fixture()
# def _config():
#     if env.upper() == 'TEST':
#         print('Test Environment')
#         return TestConfigurations
#     elif env.upper() == 'STAGE':
#         print('Stage Environment')
#         return StageConfigurations
#     else:
#         raise Exception("Unknown Environment")

@pytest.fixture()
def _driver(_config, request):
    browser_class = request.config.option.browser_name.upper()
    if browser_class == 'CHROME':
        driver = Chrome()
    elif browser_class == 'FIREFOX':
        driver = Firefox()
    elif browser_class == 'EDGE':
        driver  = Edge()
    elif browser_class == 'SAFARI':
        driver = Safari()
    else:
        raise Exception(f'{request.config.option.browser_name} not supported')
    driver.maximize_window()
    driver.get(_config.url)
    yield driver
    driver.close()

# @pytest.fixture()
# def _driver(config, browser):
#     driver =browser()
#     driver.maximize_window()
#     driver.get(config.url)
#     yield driver
#     driver.close()


# @pytest.fixture()
# def setup_teardown():
#     opts = webdriver.ChromeOptions()
#     opts.add_experimental_option('detach', True)
#     driver = webdriver.Chrome(options=opts)
#     driver.get('https://demowebshop.tricentis.com/')
#     yield driver
#     driver.close()



