# pip install PyMySQL
from tools.setLog import Logger
import pymysql
from common.rwFile import ReadConfig

logger = Logger().getlog()
class ReadMysql:
    def __init__(self):
        self.db = pymysql.connect(
            host=ReadConfig.my_ini('db_host'),
            port=int(ReadConfig.my_ini('db_port')),
            user=ReadConfig.my_ini('db_user'),
            password=ReadConfig.my_ini('db_password'),
            db=ReadConfig.my_ini('db_lib')
        )

        self.cur = self.db.cursor(cursor=pymysql.cursors.DictCursor)

    def return_all_result(self, sql):
        try:
            self.cur.execute(sql)
            data = self.cur.fetchall()
            logger.info("正在输出...{}".format(data))
            return data
        except Exception as e:
            raise e

    def return_one_result(self, sql):
        try:
            self.cur.execute(sql)
            data = self.cur.fetchone()
            logger.info("正在输出...{}".format(data))
            return data
        except Exception as e:
            raise e

    def close_mysqldb(self):
        try:
            self.db.close()
        except Exception as e:
            raise e


if __name__ == '__main__':
    db = ReadMysql()
    db.return_all_result('select * from student')
    db.close_mysqldb()
