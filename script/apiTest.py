# -*- coding: utf-8 -*-
"""
@Time    : 2021/4/19 11:20
@Author  : wanfeng
"""
import requests
from requests import session
from requests.cookies import RequestsCookieJar
from selenium import webdriver
import jsonpath

s = session()
res = s.get(url='http://192.168.0.55:36446/')
c = RequestsCookieJar()
res.cookies.update(c)




