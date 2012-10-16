#encoding:utf-8
#进行数据库的底层操作的抽象化,实现数据库的长连接,并防止数据库的重复打开

import MySQLdb
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class Database:
	def __init__(self, dbname, user, passwd):
		self.con = MySQLdb.connect(db = dbname, user = user, passwd = passwd)
		#self.cursor = self.con.cursor()

	def query(self, sql):
		self.con.query(sql)
		#self.con.commit()

	def is_exist(self, sql):
		return (self.con.cursor().execute(sql) != 0)

	def execute(self, sql):
		cursor = self.con.cursor()
		cursor.execute(sql)
		return cursor

	def close(self):
		self.con.close()

database = Database('mosquito', 'root', 'iloveparent')



