# -*- coding: utf-8 -*-
"""
@Time    : 2021/4/16 14:11
@Author  : wanfeng
"""
from time import sleep
from appium import webdriver
from common import swipeScreen
from common.saveScreenshot import take_photo_as_file
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.getElement import get_element

desired_caps ={
'deviceName':'M2004J7AC',
'appPackage':'com.tencent.mm',
'appActivity':'.ui.LauncherUI',
'platformName':'Android',
'platformVersion':'10',
'resetKeyboard': True,
'unicodeKeyboard': True,
'chromeOptions': {'androidProcess':'com.tencent.mm:appbrand0'},
'automationName': 'UiAutomator2',
'noReset': True
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
driver.implicitly_wait(10)
ac = driver.current_activity
print(ac)
driver.wait_activity(ac,1000)
swipeScreen.swipeDown(driver, n=3)
locator = (By.ID,'com.tencent.mm:id/cna1111')
get_element(driver,locator)
driver.find_elements_by_id('com.tencent.mm:id/cna')[0].click()
print (driver.contexts)
ac1 = driver.current_activity
print(ac1)
driver.wait_activity(ac1,1000)
driver.tap([(1020,450)],400)
print('成功点击')
sleep(10)
driver.close_app()
driver.quit()

# 封装toast是否存在
# driver.press_keycode(4)
# def is_toast_exist(driver,text,timeout=20,throttle=0.1):
#     try:
#         loc = ('xpath', './/*[contains(@text,{})]'.format(text))
#         print(loc)
#         WebDriverWait(driver,timeout,throttle).until(EC.presence_of_element_located(loc))
#         return True
#     except:
#         return False
# a = is_toast_exist(driver,"再按一次返回键就退出手机淘宝")
# print (a)

