# -*- coding: utf-8 -*-
"""
@Time    : 2021/4/16 14:11
@Author  : wanfeng
"""
import time
import pytest
import allure
from page.loginPage import *
from common.assertMode import Assert
from common.myDecorate import isExecute

@allure.feature('登录功能')
@allure.testcase('https://mail.qq.com/', 'qq邮箱')
class Test_login():
    @isExecute(arg=isCase1Execute)
    @allure.severity(severity_level='normal')
    @allure.story('用例1：{}'.format(case1))
    @allure.title('#{}'.format(case1))
    def test_correct_login(self, browser):
        '''正确账号、密码'''
        browser.switch_to.frame(id)
        with allure.step("输入账号"):
            ac = browser.find_element(account[0], account[1])
            ac.clear()
            ac.send_keys(case1Account[0])
        with allure.step("输入密码"):
            pw = browser.find_element(password[0], password[1])
            pw.clear()
            pw.send_keys(case1Account[1])
        with allure.step("点击登录按钮"):
            bt = browser.find_element(button[0], button[1])
            bt.click()
        with allure.step("校验结果"):
            t1 = browser.title
            t2 = "QQ邮箱"
            Assert().assertEqual(t1, t2, 'DL-DLYM-001')

    @isExecute(arg=isCase2Execute)
    @allure.story('用例2：{}'.format(case2))
    @allure.title('#{}'.format(case2))
    def test_error_account(self, browser):
        '''错误的账号'''
        browser.switch_to.frame(id)
        with allure.step("输入账号"):
            ac = browser.find_element(account[0], account[1])
            ac.clear()
            ac.send_keys(case2Account[0])
        with allure.step("输入密码"):
            pw = browser.find_element(password[0], password[1])
            pw.clear()
            pw.send_keys(case2Account[1])
        with allure.step("点击登录按钮"):
            bt = browser.find_element(button[0], button[1])
            bt.click()
            time.sleep(3)
        with allure.step("校验结果"):
            err = browser.find_element(error_msg[0], error_msg[1]).text
            text = '账号或者密码错误'
            Assert().assertIn(err,text, 'DL-DLYM-002')

if __name__ == '__main__':
    pytest.main()
