# coding:utf-8
# 配置日志
import logging
from logging import handlers
from common import configpath
BASE_DIR = configpath.ROOT_DIR
print(BASE_DIR)

'''
    Logger 记录器，暴露了应用程序代码能直接使用的接口。
    Handler 处理器，将（记录器产生的）日志记录发送至合适的目的地。
    Filter 过滤器，提供了更好的粒度控制，它可以决定输出哪些日志记录。
    Formatter 格式化器，指明了最终输出中日志记录的布局。
'''


def init_logging(logLevel=logging.INFO):
    logger = logging.getLogger()
    # 设置日志级别
    logger.setLevel(logLevel)
    # 设置日志的格式
    fmt = ('%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s - %(message)s')
    formatter = logging.Formatter(fmt)
    # 将日志输除到屏幕上的处理器
    sh = logging.StreamHandler()
    # 添加日志格式
    sh.setFormatter(formatter)
    # 设置日志存放位置
    log_path = BASE_DIR + "/logs/test.log"
    # 将日志输出到指定位置的处理器 th
    th = handlers.TimedRotatingFileHandler(filename=log_path,
                                           interval=1,
                                           backupCount=10,
                                           when='S',
                                           encoding='utf-8')
    # 添加日志格式
    th.setFormatter(formatter)
    # 添加处理器
    logger.addHandler(sh)
    logger.addHandler(th)
