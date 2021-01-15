import logging
import unittest
from time import sleep
from common import configpath
from ddt import ddt, unpack, file_data,data
import os
from app import init_logging

@ddt
class Test_001(unittest.TestCase):
    @classmethod
    def test_case01(self):
        return 1
    #@data([1,2,3],[4,5,6])
    #@file_data(configpath.yaml_path)
    @file_data(configpath.json_path)
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