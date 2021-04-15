# -*- coding: utf-8 -*-
"""
@Time    : 2021/4/14 18:00
@Author  : wanfeng

"""

from common.operateExcel import OperateExcel
from tools.setLog import Logger
log = Logger().getlog()
class Assert:
    def __init__(self):
        self.excel = OperateExcel()
        self.Pass = "pass"
        self.Fail = "fail"
        # 初始化是否通过字段
        self.isPass = None
    def assertEqual(self,a,b,id,sheet_name='登录模块用例'):
        """
        @param a:
        @param b:
        @param id: 用例编号
        @param sheet_name: Sheet表名称
        """
        try:
            log.info("预期数值为{},实际数值为{}".format(a, b))
            assert a == b
            self.isPass = self.Pass
            log.info('预期结果一致 -> 成功')
        except:
            self.isPass = self.Fail
            log.info('预期结果不一致 -> 失败')
        finally:
            self.excel.write_result(sheet_name=sheet_name, id=id,value=self.isPass)

    def assertIn(self,a,b,id,sheet_name='登录模块用例'):
        """
       @param a:
       @param b:
       @param id: 用例编号
       @param sheet_name: Sheet表名称
        """
        try:
            log.info("预期数值为{},实际数值为{}".format(a, b))
            assert a in b
            self.isPass = self.Pass
            log.info('预期结果一致 -> 成功')
        except:
            self.isPass = self.Fail
            log.info('预期结果不一致 -> 失败')
        finally:
            self.excel.write_result(sheet_name=sheet_name, id=id, value=self.isPass)




