# coding=utf-8
from appium import webdriver
des ={
'deviceName':'127.0.0.1:62001',
'platformName':'Android',
'platformVersion':'7.0.0.6',
'appPackage':'com.qzd.harddisk',
'appActivity':'com.qzd.harddisk.activity.SplashScreenActivity'
}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',des)


12345