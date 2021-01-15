import unittest

from script.p_ddt import Test_001
from utils import SendEmail
from app import init_logging
from tools import HTMLTestRunner
import logging
import os
import time
from common import configpath
logger = init_logging()
class RunCase(unittest.TestCase):
    file_path = configpath.report_path
    case_path = configpath.case_path
    logging.info(case_path)
    logging.info(file_path)
    with open(file_path,mode='wb') as f:
        #suite = unittest.TestSuite()
        #suite.addTest(unittest.TestLoader().loadTestsFromTestCase(Test_001))
        #suite = unittest.makeSuite(Test_001)
        suite = unittest.defaultTestLoader.discover(case_path,pattern='testcase*',top_level_dir=None)
        HTMLTestRunner.HTMLTestRunner(stream=f,verbosity=2,title='测试报告',description='测试结果').run(suite)
    SendEmail().send_email(file_path)
if __name__ == '__main__':
    unittest.main()




