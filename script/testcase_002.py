import logging
import unittest
from time import sleep
from ddt import ddt, unpack, file_data,data
import os
from app import init_logging
print (os.getcwd())
@ddt
class Test_001(unittest.TestCase):
    @classmethod
    def test_case01(self):
        return 1

    #@data([1,2,3],[4,5,6])
    @file_data(r'C:\Users\1111111\PycharmProjects\ApiAutoTest\data\jsondata.json')
    @unpack
    def test_case03(self,token):
        print(token)

    @unittest.skip
    def test_case02(self):
        print(Test_001.test_case01())
        print(self.test_case01())
        print(3)
        return 2

if __name__ == '__main__':
    unittest.main()

from selenium import webdriver
init_logging()
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(3)
driver.get('http://www.hao123.com')
try:
    js = 'document.documentElement.scrollTop=10000'
    driver.execute_script(js)
except Exception as e:
    logging.info(e)
    sleep(3)
driver.quit()