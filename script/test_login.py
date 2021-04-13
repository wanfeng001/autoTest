import time
from tools.setLog import Logger
from common.operateExcel import OperateExcel
import pytest
import allure
from selenium.webdriver.common.by import By
# 初始化日志
logger =Logger().getlog()
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

# 测试用例名称
case1 = OperateExcel().get_test_case(sheet_name='登录模块用例',id='DL-DLYM-001')
case2 = OperateExcel().get_test_case(sheet_name='登录模块用例',id='DL-DLYM-002')
case3 = OperateExcel().get_test_case(sheet_name='登录模块用例',id='DL-DLYM-003')
case4 = OperateExcel().get_test_case(sheet_name='登录模块用例',id='DL-DLYM-004')
case5 = OperateExcel().get_test_case(sheet_name='登录模块用例',id='DL-DLYM-005')
# 账号密码
case1Account = OperateExcel().get_account_data(sheet_name='登录模块用例',id='DL-DLYM-001')
case2Account = OperateExcel().get_account_data(sheet_name='登录模块用例',id='DL-DLYM-002')
case3Account = OperateExcel().get_account_data(sheet_name='登录模块用例',id='DL-DLYM-003')
case4Account = OperateExcel().get_account_data(sheet_name='登录模块用例',id='DL-DLYM-004')
case5Account = OperateExcel().get_account_data(sheet_name='登录模块用例',id='DL-DLYM-005')
# 是否执行
isCase1Execute = OperateExcel().get_is_execute(sheet_name='登录模块用例',id='DL-DLYM-001')
isCase2Execute = OperateExcel().get_is_execute(sheet_name='登录模块用例',id='DL-DLYM-002')
isCase3Execute = OperateExcel().get_is_execute(sheet_name='登录模块用例',id='DL-DLYM-003')
isCase4Execute = OperateExcel().get_is_execute(sheet_name='登录模块用例',id='DL-DLYM-004')
isCase5Execute = OperateExcel().get_is_execute(sheet_name='登录模块用例',id='DL-DLYM-005')







@allure.feature('登录功能')
@allure.testcase('https://mail.qq.com/', 'qq邮箱')
class Test_login():
    if isCase1Execute:
        @allure.severity(severity_level='normal')
        @allure.story('用例1：{}'.format(case1))
        @allure.title('# 登录场景测试')
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
                try:
                    err = browser.find_element(error_msg[0], error_msg[1]).text
                    logger.info(err)
                    time.sleep(1)
                    t1 = browser.title
                    assert "QQ邮箱" == t1, '没有登录进去'
                    OperateExcel().write_result(sheet_name='登录模块用例',id='DL-DLYM-001',value='pass')
                except Exception as e:
                    logger.info(e)
    else:
        logger.info('此用例IsExecute:{},不执行！'.format(isCase1Execute))

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
        pw.send_keys()
        bt = browser.find_element(button[0], button[1])
        bt.click()
        time.sleep(3)
        try:
            err = browser.find_element(error_msg[0], error_msg[1]).text
            logger.info(err)
        except Exception as e:
            logger.info(e)

    @allure.story('用例3：错误的密码')
    @allure.title('# 错误的密码')
    @pytest.mark.skip
    def test_error_password(self, browser):
        '''错误的密码'''
        browser.switch_to.frame(id)
        ac = browser.find_element(account[0], account[1])
        ac.clear()
        ac.send_keys()
        pw = browser.find_element(password[0], password[1])
        pw.clear()
        pw.send_keys(123456)
        bt = browser.find_element(button[0], button[1])
        bt.click()
        time.sleep(3)
        try:
            err = browser.find_element(error_msg[0], error_msg[1]).text
            logger.info(err)
        except Exception as e:
            logger.info(e)

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
        pw.send_keys()
        bt = browser.find_element(button[0], button[1])
        bt.click()
        try:
            err = browser.find_element(error_msg[0], error_msg[1]).text
            logger.info(err)
        except Exception as e:
            logger.info(e)

    @allure.story('用例5：密码为空')
    @allure.title('# 密码为空')
    @pytest.mark.skip
    def test_null_password(self, browser):
        '''密码为空'''
        browser.switch_to.frame(id)
        ac = browser.find_element(account[0], account[1])
        ac.clear()
        ac.send_keys()
        pw = browser.find_element(password[0], password[1])
        pw.clear()
        pw.send_keys()
        bt = browser.find_element(button[0], button[1])
        bt.click()
        try:
            err = browser.find_element(error_msg[0], error_msg[1]).text
            logger.info(err)
        except Exception as e:
            logger.info(e)

    @allure.story('用例6：失败用例截图')
    @allure.title('# 用例执行失败')
    @allure.severity(severity_level='blocker')
    @pytest.mark.skip
    def test_worry_serict(self, browser):
        '''密码为空'''
        browser.switch_to.frame(id)
        ac = browser.find_element(account[0], account[1])
        ac.clear()
        ac.send_keys()
        pw = browser.find_element(password[0], password[1])
        pw.clear()
        pw.send_keys()
        bt = browser.find_element(button[0], button[2])
        bt.click()
        try:
            err = browser.find_element(error_msg[0], error_msg[1]).text
            logger.info(err)
        except Exception as e:
            logger.info(e)


if __name__ == '__main__':
    pytest.main()
