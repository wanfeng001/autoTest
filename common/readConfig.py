import os
import configparser
# print (config_file)
class Readconfig():
    def __init__(self):
        self.config_path = os.path.join(os.getcwd(), "..\data\cfg.ini")
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

# print(Readconfig.qq_ini('email_host'))