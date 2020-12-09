# coding:utf-8
# 配置日志
import logging
from logging import handlers
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
print (BASE_DIR)
def init_logging():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    fmt = ('%(asctime)s - %(levelname)s - %(name)s - %(message)s')
    formatter = logging.Formatter(fmt)
    sh = logging.StreamHandler()
    sh.setFormatter(formatter)
    log_path = BASE_DIR +"/logs/test.log" # 日志存放位置
    th = handlers.TimedRotatingFileHandler(filename=log_path,
                                           interval=1,
                                           backupCount=3,
                                           when='S',
                                           encoding='utf-8')
    th.setFormatter(formatter)
    logger.addHandler(sh)
    logger.addHandler(th)