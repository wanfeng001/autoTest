# -*- coding: utf-8 -*-
"""
@Time    : 2021/4/14 8:50
@Author  : wanfeng
"""

from selenium.webdriver.common.by import By
from common.operateExcel import OperateExcel

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

# 测试用例名称
case1 = OperateExcel().get_test_case(sheet_name='登录模块用例', id='DL-DLYM-001')
case2 = OperateExcel().get_test_case(sheet_name='登录模块用例', id='DL-DLYM-002')
case3 = OperateExcel().get_test_case(sheet_name='登录模块用例', id='DL-DLYM-003')
case4 = OperateExcel().get_test_case(sheet_name='登录模块用例', id='DL-DLYM-004')
case5 = OperateExcel().get_test_case(sheet_name='登录模块用例', id='DL-DLYM-005')
# 账号密码
case1Account = OperateExcel().get_account_data(sheet_name='登录模块用例', id='DL-DLYM-001')
case2Account = OperateExcel().get_account_data(sheet_name='登录模块用例', id='DL-DLYM-002')
case3Account = OperateExcel().get_account_data(sheet_name='登录模块用例', id='DL-DLYM-003')
case4Account = OperateExcel().get_account_data(sheet_name='登录模块用例', id='DL-DLYM-004')
case5Account = OperateExcel().get_account_data(sheet_name='登录模块用例', id='DL-DLYM-005')
# 是否执行
isCase1Execute = OperateExcel().get_is_execute(sheet_name='登录模块用例', id='DL-DLYM-001')
isCase2Execute = OperateExcel().get_is_execute(sheet_name='登录模块用例', id='DL-DLYM-002')
isCase3Execute = OperateExcel().get_is_execute(sheet_name='登录模块用例', id='DL-DLYM-003')
isCase4Execute = OperateExcel().get_is_execute(sheet_name='登录模块用例', id='DL-DLYM-004')
isCase5Execute = OperateExcel().get_is_execute(sheet_name='登录模块用例', id='DL-DLYM-005')
