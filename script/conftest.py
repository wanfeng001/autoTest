import pytest
from selenium import webdriver
@pytest.fixture(scope='function',autouse=True)
def browser():
    global _driver
    _driver = None
    if _driver is None:
        _driver = webdriver.Chrome()
        _driver.implicitly_wait(10)
        _driver.get('https://mail.qq.com/')
        _driver.maximize_window()
    yield _driver
    _driver.quit()
    _driver = None