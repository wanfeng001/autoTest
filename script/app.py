# coding=utf-8
from appium import webdriver

from common import swipe

des ={
'deviceName':'M2004J7AC',
'platformName':'Android',
'platformVersion':'10',
'appPackage':'com.taobao.taobao',
'appActivity':'com.taobao.tao.welcome.Welcome',
'resetKeyboard':'true'
}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',des)

ac = driver.current_activity
print (ac)

driver.wait_activity(ac,10)
driver.find_element_by_id('com.taobao.taobao:id/provision_positive_button').click()
driver.find_element_by_id('com.lbe.security.miui:id/permission_allow_foreground_only_button').click()
swipe.swipeDown(driver,n=3)
driver.close_app()