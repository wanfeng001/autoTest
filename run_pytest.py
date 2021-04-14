# -*- coding: utf-8 -*-
"""
@Time    : 2021/4/14 11:59
@Author  : wanfeng

"""
import os
import pytest

pytest.main(['--alluredir=report/allure-raw','--clean-alluredir'])
adb ='allure generate report/allure-raw -o report/allure-report --clean'
os.system(adb)