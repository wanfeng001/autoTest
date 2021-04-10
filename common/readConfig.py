import os
import configparser
from common import configpath
class Readconfig:
    def __init__(self):
        self.config_path = configpath.conf_path
        self.config = configparser.ConfigParser()
        self.config.read(self.config_path,encoding='utf-8')

    # QQ邮箱配置
    @classmethod
    def qq_ini(cls,value):
        value = Readconfig().config.get('email_qq',value)
        return value

    # Mysql配置
    @classmethod
    def my_ini(cls,value):
        value =Readconfig().config.get('mysql_db',value)
        return value


if __name__ == '__main__':
    pass