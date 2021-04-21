# -*- coding: utf-8 -*-
"""
@Time    : 2021/4/16 14:11
@Author  : wanfeng
"""
# pip install PyMySQL
from tools.setLog import Logger
import pymysql
from common.rwFile import ReadConfig

logger = Logger().getlog()
class ReadMysql:
    def __init__(self):
        self.db = pymysql.connect(
            host=ReadConfig.get_db('host'),
            port=int(ReadConfig.get_db('port')),
            user=ReadConfig.get_db('user'),
            password=ReadConfig.get_db('password'),
            db=ReadConfig.get_db('db')
        )

        self.cur = self.db.cursor(cursor=pymysql.cursors.DictCursor)

    def get_data(self, sql):
        try:
            self.cur.execute(sql)
            data = self.cur.fetchall()
            logger.info(f'返回数据:{data}')
            return data
        except Exception as e:
            logger.warning(e)
            raise e

    def close_db(self):
        try:
            self.db.close()
        except Exception as e:
            logger.warning(e)
            raise e


if __name__ == '__main__':
    db = ReadMysql()
    db.get_data('select id,stu_name,stu_gender,stu_score from student')
    db.close_db()
