import time

from selenium import webdriver
from tomorrow import threads
# 装饰器
def count_time(func):
    def int_time(*args,**kwargs):
        start_time = time.time()
        func(*args,**kwargs)
        end_time= time.time()
        time1 = end_time - start_time
        print('一共花费{}秒'.format(time1))
    return  int_time()

'''
@count_time
def a():
    for i in range(1,10000):
        for y in range(i):
            pass
'''

'''
# 装饰器@property
class Test():
    @property
    def test(self):
        a = 15
        return 15
    def test1(self):
        b = 16
        return 16

print (Test().test,Test().test1())
'''

@threads(3)
def open_function(browser):
    if browser == 1:
        driver = webdriver.Chrome()
        driver.get('http://www.baidu.com')
        driver.close()
    if browser == 2:
        driver = webdriver.Chrome()
        driver.get('http://www.hao123.com')
        driver.close()
    if browser == 3:
        driver = webdriver.Chrome()
        driver.get('http://www.4399.com')
        driver.close()

def open_function1():
    driver = webdriver.Chrome()
    driver.get('http://www.baidu.com')
    driver.get('http://www.hao123.com')
    driver.get('http://www.4399.com')
    driver.close()

if __name__ == '__main__':
    list1 = [1,2,3]
    @count_time
    def a():
        for i in list1:
            open_function(i)





