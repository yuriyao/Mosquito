#encoding:utf-8
#定义用户基本信息的数据库操作
#user数据库组成:
#uName
#uPwd
#uEmail

from database import database
from mosquito.util import code

class User:
	"""存储用户基本信息"""
	def __init__(self, u_name, u_pwd, u_email):
		self.u_name = u_name
		self.u_pwd = u_pwd
		self.u_email = u_email

def u_name_logined(u_name):
	"""用户名是否已经被注册了"""
	b = database.is_exist("select * from user where uName = '%s'" % u_name)
	if b:
		return True
	return False

def u_email_logined(u_email):
	"""用户e-mail是否已经被注册了"""
	if database.is_exist("select * from user where uEmail = '%s'" % u_email):
		return True
	return False

def insert(u_name, u_pwd, u_email):
	"""插入用户基本的信息"""
	#加密用户的密码
	pwd = code.code_undecode(u_pwd)
	database.query("insert into user (uName, uPwd, uEmail) values('%s', '%s', '%s')" % (u_name, pwd, u_email))

def get_info(u_name):
	"""u_name获得用户的基本信息"""
	c = database.execute("select uName, uPwd, uEmail from user where uName = '%s'" % u_name)
	if c:
		return User(c.fetchone())
	return ''

def is_valid(u_name, u_pwd):
	"""通过用户名和密码来认证用户的合法性"""
	pwd = code.code_undecode(u_pwd)
	if database.is_exist("select * from user where uName='%s' and uPwd='%s'" % (u_name, pwd)):
		return True
	return False