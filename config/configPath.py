# -*- coding: utf-8 -*-
"""
@Time    : 2021/4/16 14:11
@Author  : wanfeng
"""
import os
from time import strftime

# 项目根目录路径
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 日志存放路径
LOG_PATH = os.path.join(ROOT_DIR, 'logs')
# 配置文件存放路径
CONFIGDATA_PATH = os.path.join(ROOT_DIR, 'config', 'configData.ini')
# Excel用例存放路径
EXCEL_PATH = os.path.join(ROOT_DIR, 'data', 'Mes快速建模测试用例.xlsx')
# json格式数据文件存放路径
JSON_PATH = os.path.join(ROOT_DIR, 'data', 'jsondata.json')
# yaml格式数据文件存放路径
YAML_PATH = os.path.join(ROOT_DIR, 'data', 'yamldata.yaml')
# 图片存放路径
PICTURE_PATH = os.path.join(ROOT_DIR, 'screenshot', '1-{}.png'.format(strftime('%Y%m%d%H%M%S')))
# 用例脚本存放路径
SCRIPT_PATH = os.path.join(ROOT_DIR, 'script')
# 报告存放路径
REPORT_PATH = os.path.join(ROOT_DIR, 'report', 'test_report-{}.html'.format(strftime('%Y%m%d%H%M%S')))
# 驱动存放位置
CHROME_PATH = os.path.join(ROOT_DIR, 'config', 'driver', 'chromedriver.exe')
