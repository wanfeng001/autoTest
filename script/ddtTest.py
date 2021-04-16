# -*- coding: utf-8 -*-
"""
@Time    : 2021/4/16 14:11
@Author  : wanfeng
"""
import unittest
from ddt import ddt, unpack, file_data, data
from config import configPath


@ddt
class Test_001(unittest.TestCase):

    # 数据驱动 - 读取json文件
    @file_data(configPath.json_path)
    @unpack
    def test_case01(self, username, password):
        print(username, password)

    # 数据驱动 - 读取yaml文件
    #@file_data(configPath.yaml_path)
    # @unpack
    # def test_case01(self,**kwargs):
    #     print(kwargs)

    @classmethod
    def test_case02(self):
        return "test"

    # 跳过用例
    @unittest.skip
    def test_case03(self):
        print(Test_001.test_case02())
        print(self.test_case02())


if __name__ == '__main__':
    unittest.main()
