import time
import logging
from app import init_logging
from selenium import webdriver
from common import configpath
from common import readExcel
from common import getTime
import pytest
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

# 账号元素
account = (By.XPATH, '//*[@id="u"]')
# 密码元素
password = (By.XPATH, '//*[@id="p"]')
# 登录按钮
button = (By.XPATH, '//*[@id="login_button"]')
# 错误信息提示
error_msg = (By.XPATH, '//*[@id="err_m"]')
# iframe
id = 'login_frame'
# 断言值:名字
name = (By.XPATH, '//*[@id="useralias"]')
# 滑动按钮 22.5px 193.5px  移动距离 171px
hua_button = (By.XPATH, '//*[@id="tcaptcha_drag_thumb"]')


@allure.feature('登录模块')
class Test_login():
    @allure.title('# 正确账号、密码')
    def test_correct_login(self, browser):
        browser.switch_to.frame(id)
        ac = browser.find_element(account[0], account[1])
        ac.clear()
        ac.send_keys(configpath.account)
        pw = browser.find_element(password[0], password[1])
        pw.clear()
        pw.send_keys(configpath.password)
        bt = browser.find_element(button[0], button[1])
        bt.click()
        try:
            na = browser.find_element(name[0], name[1]).text
            print(na)
            assert "挽风" in na, '这里断了'
        except Exception as e:
            print(e)

    # 错误的账号
    # @pytest.mark.skip
    def test_error_account(self, browser):
        browser.switch_to.frame(id)
        ac = browser.find_element(account[0], account[1])
        ac.clear()
        ac.send_keys(1)
        pw = browser.find_element(password[0], password[1])
        pw.clear()
        pw.send_keys(configpath.password)
        bt = browser.find_element(button[0], button[1])
        bt.click()
        time.sleep(3)
        try:
            err = browser.find_element(error_msg[0], error_msg[1]).text
            print(err)
        except Exception as e:
            print(e)

    # 错误的密码
    # @pytest.mark.skip
    def test_error_password(self, browser):
        browser.switch_to.frame(id)
        ac = browser.find_element(account[0], account[1])
        ac.clear()
        ac.send_keys(configpath.account)
        pw = browser.find_element(password[0], password[1])
        pw.clear()
        pw.send_keys(123456)
        bt = browser.find_element(button[0], button[1])
        bt.click()
        time.sleep(3)
        try:
            err = browser.find_element(error_msg[0], error_msg[1]).text
            print(err)
        except Exception as e:
            print(e)

    # 账号为空
    # @pytest.mark.skip
    def test_null_account(self, browser):
        browser.switch_to.frame(id)
        ac = browser.find_element(account[0], account[1])
        ac.clear()
        ac.send_keys()
        pw = browser.find_element(password[0], password[1])
        pw.clear()
        pw.send_keys(configpath.password)
        bt = browser.find_element(button[0], button[1])
        bt.click()
        try:
            err = browser.find_element(error_msg[0], error_msg[1]).text
            print(err)
        except Exception as e:
            print(e)

    # 密码为空
    # @pytest.mark.skip
    def test_null_password(self, browser):
        browser.switch_to.frame(id)
        ac = browser.find_element(account[0], account[1])
        ac.clear()
        ac.send_keys(configpath.account)
        pw = browser.find_element(password[0], password[1])
        pw.clear()
        pw.send_keys()
        bt = browser.find_element(button[0], button[1])
        bt.click()
        try:
            err = browser.find_element(error_msg[0], error_msg[1]).text
            print(err)
        except Exception as e:
            print(e)


if __name__ == '__main__':
    pytest.main(['-s'])
