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
log_path = os.path.join(ROOT_DIR, 'logs')
# 配置文件存放路径
configdata_path = os.path.join(ROOT_DIR, 'config','configData.ini')
# Excel用例存放路径
excel_path = os.path.join(ROOT_DIR,'data','Mes快速建模测试用例.xlsx')
# json格式数据文件存放路径
json_path = os.path.join(ROOT_DIR, 'data','jsondata.json')
# yaml格式数据文件存放路径
yaml_path = os.path.join(ROOT_DIR, 'data','yamldata.yaml')
# 图片存放路径
picture_path = os.path.join(ROOT_DIR, 'screenshot','1-{}.png'.format(strftime('%Y%m%d%H%M%S')))
# 用例脚本存放路径
script_path = os.path.join(ROOT_DIR, 'script')
# 报告存放路径
report_path = os.path.join(ROOT_DIR, 'report','test_report-{}.html'.format(strftime('%Y%m%d%H%M%S')))
# 驱动存放位置
chrome_path = os.path.join(ROOT_DIR,'config','driver','chromedriver.exe')
