# coding:utf-8
# 配置日志
import logging
from common import configpath
from common.getTime import GetTime

'''
    Logger 记录器，暴露了应用程序代码能直接使用的接口。
    Handler 处理器，将（记录器产生的）日志记录发送至合适的目的地。
    Filter 过滤器，提供了更好的粒度控制，它可以决定输出哪些日志记录。
    Formatter 格式化器，指明了最终输出中日志记录的布局。
'''

class Logger:
    def __init__(self, CmdLevel=logging.INFO, FileLevel=logging.INFO):
        BASE_DIR = configpath.ROOT_DIR
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)  # 设置日志默认级别为DEBUG
        fmt = logging.Formatter('%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s - %(message)s')  # 设置日志输出格式
        currTime = GetTime.get_current_time()  # 格式化当前时间
        log_path = BASE_DIR + "\\logs"  # 设置日志文件保存路径

        print('得到的日志路径为：', log_path)
        log_name = log_path + currTime + '.log'  # 设置日志文件名称

        # 设置由文件输出
        fh = logging.FileHandler(log_name, encoding='utf-8')  # 采用utf-8字符集格式防止出现中文乱码
        fh.setFormatter(fmt)
        fh.setLevel(FileLevel)  # 日志级别为INFO

        # 设置日志由控制台输出
        sh = logging.StreamHandler()
        sh.setFormatter(fmt)
        sh.setLevel(CmdLevel)

        self.logger.addHandler(fh)  # 添加handler
        self.logger.addHandler(sh)  # 添加handler


    def getlog(self):
        return self.logger