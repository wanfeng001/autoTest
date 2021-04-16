# -*- coding: utf-8 -*-
"""
@Time    : 2021/4/16 14:11
@Author  : wanfeng
"""
from config import configPath

filename = configPath.picture_path

def take_photo_as_file(driver):
    driver.save_screenshot(filename=filename)

def take_photo_as_base64(driver):
    driver.get_screenshot_as_png(filename=filename)