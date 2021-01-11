# pip install PyMySQL
from app import init_logging
import logging
init_logging()
import pymysql
from common.readConfig import Readconfig

db =pymysql.connect(
    host = Readconfig.my_ini('db_host'),
    port = int(Readconfig.my_ini('db_port')),
    user = Readconfig.my_ini('db_user'),
    password = Readconfig.my_ini('db_password'),
    db = Readconfig.my_ini('db_lib')
)

cur = db.cursor(cursor=pymysql.cursors.DictCursor)
cur.execute('select * from student')
data = cur.fetchall()
db.close()
logging.info("正在输出...{}".format(data))