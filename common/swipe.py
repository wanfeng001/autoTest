from time import sleep

from appium import webdriver
des ={
'deviceName':'M2004J7AC',
'platformName':'Android',
'platformVersion':'10',
'appPackage':'com.taobao.taobao',
'appActivity':'com.taobao.tao.welcome.Welcome',
'resetKeyboard':'true'
}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',des)

def swipeDown(driver,t=500,n=1):
    l = driver.get_window_size()
    x1= l['width']* 0.5
    y1= l['height']* 0.25
    y2= l['height']* 0.8
    for i in range(n):
        driver.swipe(x1,y1,x1,y2,t)

def swipeUp(driver,t=500,n=1):
    l = driver.get_window_size()
    x1= l['width']* 0.5
    y1= l['height']* 0.75
    y2= l['height']* 0.25
    for i in range(n):
        driver.swipe(x1,y1,x1,y2,t)

def swipeRight(driver,t=500,n=1):
    l = driver.get_window_size()
    x1= l['width']* 0.5
    x2= l['width']* 0.75
    y1= l['height']* 0.5
    for i in range(n):
        driver.swipe(x1,y1,x2,y1,t)

def swipeLeft(driver,t=500,n=1):
    l = driver.get_window_size()
    x1= l['width']* 0.5
    x2= l['width']* 0.25
    y1= l['height']* 0.5
    for i in range(n):
        driver.swipe(x1,y1,x2,y1,t)

if __name__ == "__main__":
    ac = driver.current_activity
    driver.wait_activity(ac, 20)
    driver.find_element_by_id('com.taobao.taobao:id/provision_positive_button').click()
    driver.find_element_by_id('com.lbe.security.miui:id/permission_allow_foreground_only_button').click()
    sleep(3)
    swipeDown(driver,n=2)
    sleep(3)
    swipeRight(driver,n=2)
    sleep(3)
    swipeLeft(driver,n=2)
    driver.close_app()

