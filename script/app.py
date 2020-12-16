# coding=utf-8
from time import sleep

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
ac1 = driver.current_activity
sleep(2)
driver.find_element_by_id('com.lbe.security.miui:id/permission_allow_foreground_only_button').click()
# swipe.swipeDown(driver,n=3)
ac2 = driver.current_activity
driver.wait_activity(ac2,20)
l = driver.get_window_size()
x1=l['width']*0.8
y1=l['height']*0.1
x2=l['width']*0.2
for i in range(2):
    driver.swipe(x1,y1,x2,y1,500)
sleep(10)
driver.close_app()