import os
from time import strftime
''' 存放项目路径 '''
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
log_path = os.path.join(ROOT_DIR,'logs')
conf_path = os.path.join(ROOT_DIR,'data\cfg.ini')
excel_path = os.path.join(ROOT_DIR,'data\\126MailContact.xlsx')
json_path = os.path.join(ROOT_DIR,'data\jsondata.json')
yaml_path = os.path.join(ROOT_DIR,'data\yamldata.yaml')
picture_path = os.path.join(ROOT_DIR,'screenshot/1-{}.png'.format(strftime('%Y%m%d%H%M%S')))
case_path = os.path.join(ROOT_DIR,'script')
report_path = os.path.join(ROOT_DIR,'report\\test_report-{}.html'.format(strftime('%Y%m%d%H%M%S')))
