from time import sleep
from appium import webdriver
from common import swipe

desired_caps ={
'deviceName':'M2004J7AC',
'platformName':'Android',
'platformVersion':'10',
'appPackage':'com.tencent.mm',
'appActivity':'.ui.LauncherUI',
'resetKeyboard': True,
'unicodeKeyboard': True,
'chromeOptions': {'androidProcess': 'com.tencent.mm:appbrand0'},
'automationName': 'UiAutomator2',
'noReset': True
}

driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
handlers = driver.contexts
print(handlers)
sleep(10)
driver.close_app()
driver.quit()