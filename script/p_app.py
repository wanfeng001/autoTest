# coding=utf-8
import os
import time
from time import sleep
from selenium import webdriver
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from common import swipe
from common.saveScreenshot import take_photo
from common.waitElement import wait_element

desired_caps ={
'deviceName':'M2004J7AC',
'platformName':'Android',
'platformVersion':'10',
'appPackage':'com.taobao.taobao',
'appActivity':'com.taobao.tao.welcome.Welcome',
'resetKeyboard': True,
'unicodeKeyboard': True,
'automationName':'UiAutomator2',
'noReset': True
}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)

driver.implicitly_wait(10)
ac = driver.current_activity
print (ac)
driver.wait_activity(ac,10)
driver.find_element_by_id('com.taobao.taobao:id/uik_mdButtonDefaultPositive').click()
driver.find_element_by_id('com.taobao.taobao:id/provision_positive_button').click()
ac1 = driver.current_activity
driver.find_element_by_id('com.lbe.security.miui:id/permission_allow_foreground_only_button').click()
t = driver.contexts
print (t)

'''
# 向下滑动
swipe.swipeDown(driver,n=3)

# 滑动
l = driver.get_window_size()
x1=l['width']*0.8
y1=l['height']*0.1
x2=l['width']*0.2
for i in range(2):
    driver.swipe(x1,y1,x2,y1,500)
sleep(10)
'''

'''
定位toast
driver.press_keycode(4)
toast_loc= ('xpath','.//*[contains(@text,“再按一次返回键退出手机淘宝”)]')
t = WebDriverWait(driver,20,0.1).until(EC.presence_of_element_located(toast_loc))
print (t)
'''
'''
# 封装toast是否存在
driver.press_keycode(4)
def is_toast_exist(driver,text,timeout=20,throttle=0.1):
    try:
        loc = ('xpath', './/*[contains(@text,{})]'.format(text))
        print(loc)
        WebDriverWait(driver,timeout,throttle).until(EC.presence_of_element_located(loc))
        return True
    except:
        return False
a = is_toast_exist(driver,"再按一次返回键就退出手机淘宝")
print (a)
'''


'''
# 点击第一张图片
ac2 =driver.current_activity
print (ac2)
driver.wait_activity(ac2,20)
try:
    driver.implicitly_wait(10)
    ele = driver.find_elements_by_class_name("android.widget.ImageView")[1].click()
    print (ele)
    sleep(3)
except Exception as e:
    print(e)
'''

ac = driver.current_activity
print (ac)
driver.wait_activity(ac,10)
# 点击搜索框
driver.tap([(431,140),(200,140)],500)

def search_button(driver):
    ele = driver.find_element_by_accessibility_id('搜索')
    return  ele

def search_kuang(driver):
    ele = driver.find_element_by_id('com.taobao.taobao:id/searchEdit')
    return  ele

def search_kuanghou(driver):
    ele = driver.find_element_by_id('com.taobao.taobao:id/search_bar_wrapper')
    return ele
'''
# 封装元素等待
def wait_element(driver,locator,timeout=10):
    try:
        ele = WebDriverWait(driver,timeout,0.1).until(EC.presence_of_element_located(locator))
        return ele
    except Exception as e:
        take_photo(driver)
        print ('找不到指定元素')
'''

search_kuang(driver).send_keys('测试')
search_button(driver).click()
search_kuanghou(driver).click()
loc =(By.ID,'com.taobao.taobao:id/searchEdit')
wait_element(driver,loc).send_keys('测试66')
search_button(driver).click()
sleep(5)


'''
ele = 'new UiSelector().text()' 
ele = 'new UiSelector().textContains()'
ele = 'new UiSelector().resourceId()'
ele = 'new UiSelector().description("content-desc")'
driver.find_elements_by_android_uiautomator()
'''
'''
# Id + text定位
ele = 'resourceId().text()' 
# 父子关系childSelector
ele = 'resourceId().childSelector()' 
# 兄弟关系fromParent
ele = 'resourceId().fromParent()'
'''

driver.close_app()
