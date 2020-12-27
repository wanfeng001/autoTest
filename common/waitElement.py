from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from common.saveScreenshot import take_photo


def wait_element(driver,locator,timeout=10):
    try:
        ele = WebDriverWait(driver,timeout,0.1).until(EC.presence_of_element_located(locator))
        return ele
    except Exception as e:
        take_photo(driver)
        print ('找不到指定元素')
