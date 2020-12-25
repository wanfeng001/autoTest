import os
from time import strftime
filedir = os.path.abspath(os.path.join(os.getcwd(), "./.."))
filename = os.path.join(filedir,'screenshot/1-{}.png'.format(strftime('%Y%m%d%H%M%S')))

def take_photo(driver):
    driver.save_screenshot(filename=filename)
