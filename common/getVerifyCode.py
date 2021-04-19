# -*- coding: utf-8 -*-
"""
@Time    : 2021/4/16 16:22
@Author  : wanfeng
"""
#pip install Pillow
#pip install pyocr
#pip install pytesseract
import time

from selenium import webdriver
from PIL import Image
import pytesseract
from config.configPath import *
import cv2 as cv

from tools.setLog import Logger


class VerifyCode:
    @classmethod
    def getCode(cls):
        try:
            chrome_driver = chrome_path
            os.environ["webdriver.Chrome.driver"] = chrome_driver
            cls.driver = webdriver.Chrome(chrome_driver)
            cls.driver.maximize_window()
            cls.driver.implicitly_wait(10)
            cls.driver.get("http://192.168.0.55:8888")
            account = cls.driver.find_element_by_xpath('//div[@class="el-input el-input--small el-input--prefix"]/input')
            account.clear()
            account.send_keys('admin')
            password = cls.driver.find_element_by_xpath('//div[@class="el-input el-input--small el-input--prefix el-input--suffix"]/input')
            password.clear()
            password.send_keys('admin')
            cls.driver.save_screenshot(picture_path)
            imgElement = cls.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/form/div[3]/div/div/div[2]/div/img')    #定位验证码
            location = imgElement.location     #获取验证码X,Y的坐标
            size = imgElement.size             #获取验证码的长宽
            rangle = (int(location['x']),int(location['y']),int(location['x']+size['width']),int(location['y']+size['height']))  #写成我们需要的位置坐标
            image = Image.open((picture_path))     #打开截图
            frame4 = image.crop(rangle)                #使用image的crop函数，从截图中再次截取我们的区域
            frame4.save(picture_path)
            verifycode = Image.open(picture_path)
            text = pytesseract.image_to_string(verifycode).strip() #  使用image_to_string识别验证码
            print(text)
            time.sleep(3)
        except Exception as e:
            raise e
        finally:
            cls.driver.quit()

VerifyCode.getCode()