# -*- coding: utf-8 -*-
"""
@Time    : 2021/4/16 14:11
@Author  : wanfeng
"""
import os
import pytest
from selenium import webdriver
from py._xmlgen import html
import allure
from config import configPath

from config import configPath
driver_path = configPath.CHROME_PATH
@pytest.fixture(scope='function',autouse=True)
def browser(headless=True):
    # 静默执行
    option = webdriver.ChromeOptions()
    option.add_argument('headless') if headless else None
    global _driver
    _driver = None
    if _driver is None:
        _driver = webdriver.Chrome(driver_path,chrome_options=option)
        _driver.implicitly_wait(10)
        _driver.get('https://mail.qq.com/')
        _driver.maximize_window()
    yield _driver
    _driver.quit()
    _driver = None

# 钩子函数 添加工作环境 environment.properities
def pytest_sessionfinish():
    r = configPath.ROOT_DIR
    with open(r + "/report/allure-raw/environment.properties", "w") as f:
        f.write("browser=chrome\nautor=wanfeng\ndomain=https://mail.qq.com/")


# allure 失败用例自动截图
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    '''
    获取每个用例状态的钩子函数
    :param item:
    :param call:
    :return:
    '''
    # 获取钩子方法的调用结果
    outcome = yield
    rep = outcome.get_result()
    # 仅仅获取用例call 执行结果是失败的情况, 不包含 setup/teardown
    if rep.when == "call" and rep.failed:
        mode = "a" if os.path.exists("failures") else "w"
        with open("failures", mode) as f:
            # let's also access a fixture for the fun of it
            if "tmpdir" in item.fixturenames:
                extra = " (%s)" % item.funcargs["tmpdir"]
            else:
                extra = ""
            f.write(rep.nodeid + extra + "\n")
        # 添加allure报告截图
        if hasattr(_driver, "get_screenshot_as_png"):
            with allure.step('添加失败截图'):
                allure.attach(_driver.get_screenshot_as_png(), "失败截图", allure.attachment_type.PNG)

# pytest-html 失败用例自动截图
@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """当测试失败的时候，自动截图，展示到html报告中"""
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    report.description = str(item.function.__doc__)
    report.nodeid = report.nodeid.encode("utf-8").decode("unicode_escape")
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_")+".png"
            screen_img = _capture_screenshot()
            if file_name:
                html = '<div><img src="data:image/png;base64,%s" alt="screenshot" style="width:600px;height:300px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % screen_img
                extra.append(pytest_html.extras.html(html))
        report.extra = extra

def _capture_screenshot():
    '''截图保存为base64'''
    return _driver.get_screenshot_as_base64()

@pytest.mark.optionalhook
def pytest_html_results_summary(prefix):
    prefix.extend([html.p("所属部门: 测试部门")])
    prefix.extend([html.p("测试人员: 浩涛")])

@pytest.mark.optionalhook
def pytest_html_results_table_header(cells):
    cells.insert(1, html.th('Description'))

@pytest.mark.optionalhook
def pytest_html_results_table_row(report, cells):
    cells.insert(1, html.td(report.description))