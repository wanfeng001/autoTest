from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from common.saveScreenshot import take_photo_as_file


def get_element(driver,locator,timeout=10):
    try:
        ele = WebDriverWait(driver,timeout,0.1).until(EC.presence_of_element_located(locator))
        return ele
    except Exception as e:
        take_photo_as_file(driver)
        print ('找不到指定元素')
        print(e)
