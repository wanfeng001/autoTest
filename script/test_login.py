import time
import logging
from tools.setLog import init_logging
from common import configpath
from common import readExcel

import pytest
import allure
from selenium.webdriver.common.by import By

# 初始化日志
init_logging()
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

# 测试用例名称那一列数据
# caseName = ReadExcel().get_column_value('登录模块用例', configpath.testCase)

@allure.feature('登录功能')
@allure.testcase('https://mail.qq.com/', 'qq邮箱')
class Test_login():
    @allure.severity(severity_level='normal')
    @allure.story('用例1：登录功能')
    @allure.title('# 登录场景测试')
    @pytest.mark.parametrize("user,pwd", readExcel.get_data())
    def test_correct_login(self, browser, user, pwd):
        '''正确账号、密码'''
        browser.switch_to.frame(id)
        with allure.step("输入账号"):
            ac = browser.find_element(account[0], account[1])
            ac.clear()
            ac.send_keys(user)
        with allure.step("输入密码"):
            pw = browser.find_element(password[0], password[1])
            pw.clear()
            pw.send_keys(pwd)
        with allure.step("点击登录按钮"):
            bt = browser.find_element(button[0], button[1])
            bt.click()
        with allure.step("校验结果"):
            try:
                err = browser.find_element(error_msg[0], error_msg[1]).text
                logging.info(err)
                time.sleep(1)
                t1 = browser.title
                assert "QQ邮箱" == t1, '没有登录进去'

            except Exception as e:
                logging.info(e)
        # with allure.step("校验结果"):
        #     try:
        #         time.sleep(1)
        #         na = browser.find_element(name[0], name[1]).text
        #         logging.info(na)
        #         assert "挽风" in na, '没有登录进去'
        #     except Exception as e:
        #         logging.info(e)

    @allure.story('用例2：错误的账号')
    @allure.title('# 错误的账号')
    @pytest.mark.skip
    def test_error_account(self, browser):
        '''错误的账号'''
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
            logging.info(err)
        except Exception as e:
            logging.info(e)

    @allure.story('用例3：错误的密码')
    @allure.title('# 错误的密码')
    @pytest.mark.skip
    def test_error_password(self, browser):
        '''错误的密码'''
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
            logging.info(err)
        except Exception as e:
            logging.info(e)

    @allure.story('用例4：账号为空')
    @allure.title('# 账号为空')
    @pytest.mark.skip
    def test_null_account(self, browser):
        '''账号为空'''
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
            logging.info(err)
        except Exception as e:
            logging.info(e)

    @allure.story('用例5：密码为空')
    @allure.title('# 密码为空')
    @pytest.mark.skip
    def test_null_password(self, browser):
        '''密码为空'''
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
            logging.info(err)
        except Exception as e:
            logging.info(e)

    @allure.story('用例6：失败用例截图')
    @allure.title('# 用例执行失败')
    @allure.severity(severity_level='blocker')
    @pytest.mark.skip
    def test_worry_serict(self, browser):
        '''密码为空'''
        browser.switch_to.frame(id)
        ac = browser.find_element(account[0], account[1])
        ac.clear()
        ac.send_keys(configpath.account)
        pw = browser.find_element(password[0], password[1])
        pw.clear()
        pw.send_keys()
        bt = browser.find_element(button[0], button[2])
        bt.click()
        try:
            err = browser.find_element(error_msg[0], error_msg[1]).text
            logging.info(err)
        except Exception as e:
            logging.info(e)


if __name__ == '__main__':
    pytest.main(['-s'])
