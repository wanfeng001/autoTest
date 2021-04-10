import unittest

from tools.setEmail import SendEmail
from tools.setLog import Logger
from tools import HTMLTestRunner
from common import configpath
logger = Logger().getlog()
class RunCase(unittest.TestCase):
    file_path = configpath.report_path
    case_path = configpath.case_path
    with open(file_path,mode='wb') as f:
        #suite = unittest.TestSuite()
        #suite.addTest(unittest.TestLoader().loadTestsFromTestCase(Test_001))
        #suite = unittest.makeSuite(Test_001)
        suite = unittest.defaultTestLoader.discover(case_path,pattern='testcase*',top_level_dir=None)
        HTMLTestRunner.HTMLTestRunner(stream=f,verbosity=2,title='测试报告',description='测试结果').run(suite)
    SendEmail().send_email(file_path)
if __name__ == '__main__':
    unittest.main()