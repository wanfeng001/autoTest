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

    def select_data(self, sql):
        try:
            self.cur.execute(sql)
            data = self.cur.fetchall()
            logger.info(f'返回数据:{data}')
            return data
        except Exception as e:
            logger.warning(e)
            raise e

    def close_mysqldb(self):
        try:
            self.db.close()
        except Exception as e:
            raise e


if __name__ == '__main__':
    db = ReadMysql()
    db.select_data('select id,stu_name,stu_gender,stu_score from student')
    db.close_mysqldb()
