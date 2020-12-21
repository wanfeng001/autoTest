from appium import webdriver
from common import swipe

desired_caps ={
'deviceName':'M2004J7AC',
'platformName':'Android',
'platformVersion':'10',
'appPackage':'com.tencent.mm',
'appActivity':'.ui.LauncherUI',
# 'resetKeyboard': True,
# 'unicodeKeyboard': True,
'automationName': 'Appium',
'chromeOptions': {'androidProcess': 'com.tencent.mm:appbrand0'},
'noReset': True
}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
swipe.swipeDown(driver,n=3)
driver.close_app()