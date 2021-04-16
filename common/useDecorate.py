# -*- coding: utf-8 -*-
"""
@Time    : 2021/4/15 14:38
@Author  : wanfeng
"""
from functools import wraps
# 带参数装饰器设置,装饰器名字：isExecute
def isExecute(arg):
    """
    @param arg: 布尔值（1=执行,0=不执行）
    @return:
    """
    def warpperMiddle(fn):
        # 定义一个嵌套函数
        @wraps(fn)
        def warpper(*args, **kwargs):
            if arg == True:
                fn(*args, **kwargs)
            else:
                raise TypeError('输入的参数只能为布尔值,请填入正确的参数')
            return fn
        return warpper
    return warpperMiddle