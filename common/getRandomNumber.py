# -*- coding: utf-8 -*-
"""
@Time    : 2021/4/16 14:11
@Author  : wanfeng
"""
import random
import string

class creatNumber:
    @staticmethod
    def getPhoneNumber():
        s = ''.join(random.sample('123456789', 9))
        f = random.choice('3579')
        data = '1' + f + s
        return data

    @staticmethod
    def getAccount(len):
        a = ''.join(random.sample(string.ascii_letters, 1))
        ran_str = ''.join(random.sample(string.ascii_letters + string.digits, len - 1))
        data = a + ran_str
        return data

