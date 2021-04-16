# -*- coding: utf-8 -*-
"""
@Time    : 2021/4/16 14:11
@Author  : wanfeng
"""
import time
from datetime import date

class GetTime:
    @staticmethod
    def get_current_day():
        try:
            current_day = date.today()
        except Exception as e:
            raise e
        else:
            return str(current_day)

    @staticmethod
    def get_current_time():
        try:
            current_time = time.strftime('%Y-%m-%d_%H-%M-%S')
        except Exception as e:
            raise e
        else:
            return str(current_time)

