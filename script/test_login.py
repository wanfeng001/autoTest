import time
from tools.setLog import Logger
import pytest
import allure
from page.loginPage import *
from common.assertMode import Assert
import functools


@allure.feature('登录功能')
@allure.testcase('https://mail.qq.com/', 'qq邮箱')
class Test_login():
    if isCase1Execute:
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
    else:
        print("此用例不执行")

    if isCase2Execute:
        @allure.story('用例2：{}'.format(case2))
        @allure.title('#{}'.format(case2))
        # @pytest.mark.skip
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
                text = '请输入你的密码'
                Assert().assertIn(err, text, 'DL-DLYM-001')
    else:
        print("此用例不执行")

    # if isCase3Execute:
    #     @allure.story('用例3：{}'.format(case3))
    #     @allure.title('#{}'.format(case3))
    #     # @pytest.mark.skip
    #     def test_error_password(self, browser):
    #         '''错误的密码'''
    #         browser.switch_to.frame(id)
    #         ac = browser.find_element(account[0], account[1])
    #         ac.clear()
    #         ac.send_keys(case3Account[0])
    #         pw = browser.find_element(password[0], password[1])
    #         pw.clear()
    #         pw.send_keys(case3Account[1])
    #         bt = browser.find_element(button[0], button[1])
    #         bt.click()
    #         time.sleep(3)
    #         try:
    #             err = browser.find_element(error_msg[0], error_msg[1]).text
    #             logger.info(err)
    #             time.sleep(1)
    #             t1 = browser.title
    #             assert "QQ邮箱" == t1, '没有登录进去'
    #         except Exception as e:
    #             OperateExcel().write_result(sheet_name='登录模块用例', id='DL-DLYM-003', value='fail')
    #             logger.info(e)
    # else:
    #     logger.info('此用例IsExecute:{},不执行！'.format(isCase3Execute))
    #
    # if isCase4Execute:
    #     @allure.story('用例4：{}'.format(case4))
    #     @allure.title('#{}'.format(case4))
    #     # @pytest.mark.skip
    #     def test_null_account(self, browser):
    #         '''账号为空'''
    #         browser.switch_to.frame(id)
    #         ac = browser.find_element(account[0], account[1])
    #         ac.clear()
    #         ac.send_keys(case4Account[0])
    #         pw = browser.find_element(password[0], password[1])
    #         pw.clear()
    #         pw.send_keys(case4Account[1])
    #         bt = browser.find_element(button[0], button[1])
    #         bt.click()
    #         try:
    #             err = browser.find_element(error_msg[0], error_msg[1]).text
    #             logger.info(err)
    #             time.sleep(1)
    #             t1 = browser.title
    #             assert "QQ邮箱" == t1, '没有登录进去'
    #         except Exception as e:
    #             OperateExcel().write_result(sheet_name='登录模块用例', id='DL-DLYM-004', value='fail')
    #             logger.info(e)
    # else:
    #     logger.info('此用例IsExecute:{},不执行！'.format(isCase4Execute))
    #
    # if isCase5Execute:
    #     @allure.story('用例5：{}'.format(case5))
    #     @allure.title('#{}'.format(case5))
    #     # @pytest.mark.skip
    #     def test_null_password(self, browser):
    #         '''密码为空'''
    #         browser.switch_to.frame(id)
    #         ac = browser.find_element(account[0], account[1])
    #         ac.clear()
    #         ac.send_keys(case5Account[0])
    #         pw = browser.find_element(password[0], password[1])
    #         pw.clear()
    #         pw.send_keys(case5Account[1])
    #         bt = browser.find_element(button[0], button[1])
    #         bt.click()
    #         try:
    #             err = browser.find_element(error_msg[0], error_msg[1]).text
    #             logger.info(err)
    #             time.sleep(1)
    #             t1 = browser.title
    #             assert "QQ邮箱" == t1, '没有登录进去'
    #         except Exception as e:
    #             OperateExcel().write_result(sheet_name='登录模块用例', id='DL-DLYM-005', value='fail')
    #             logger.info(e)
    # else:
    #     logger.info('此用例IsExecute:{},不执行！'.format(isCase5Execute))


if __name__ == '__main__':
    pytest.main()
