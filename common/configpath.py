import os
from time import strftime

''' 存放项目路径 '''
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
log_path = os.path.join(ROOT_DIR, 'logs')
conf_path = os.path.join(ROOT_DIR, 'data\cfg.ini')
excel_path = os.path.join(ROOT_DIR, 'data\\126MailContact.xlsx')
excel1_path = os.path.join(ROOT_DIR,'data\\Mes快速建模测试用例.xlsx')
json_path = os.path.join(ROOT_DIR, 'data\jsondata.json')
yaml_path = os.path.join(ROOT_DIR, 'data\yamldata.yaml')
picture_path = os.path.join(ROOT_DIR, 'screenshot\\1-{}.png'.format(strftime('%Y%m%d%H%M%S')))
case_path = os.path.join(ROOT_DIR, 'script')
report_path = os.path.join(ROOT_DIR, 'report\\test_report-{}.html'.format(strftime('%Y%m%d%H%M%S')))

absfile = os.path.abspath(__file__)
print(absfile)
abdfiledir = os.path.dirname(os.path.abspath(__file__))
print(abdfiledir)
print(ROOT_DIR)

''' EXCEL 列名对应位置 '''
testCase = 3
priority = 4
Account = 5
Password = 6
Expect = 7
isExecute = 8
