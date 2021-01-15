import os
from time import strftime
filedir = os.path.abspath(os.path.join(os.getcwd(), "./.."))
filename = os.path.join(filedir,'screenshot/1-{}.png'.format(strftime('%Y%m%d%H%M%S')))

def take_photo_as_file(self,driver):
    driver.save_screenshot(filename=filename)

def take_photo_as_base64(self,driver):
    driver.get_screenshot_as_png(filename=filename)