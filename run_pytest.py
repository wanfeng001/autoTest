# -*- coding: utf-8 -*-
"""
@Time    : 2021/4/14 11:59
@Author  : wanfeng

"""
import os
import pytest

# pytest程序调用
pytest.main(['-n=3','--alluredir=report/allure-raw','--clean-alluredir'])
# 执行CMD命令
cmd ='allure generate report/allure-raw -o report/allure-report --clean'
os.system(cmd)
