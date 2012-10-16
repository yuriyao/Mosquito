#encoding:utf-8
from database import database
#数据库组成:
#uName varchar(15) 外键
#realName varchar(16)
#sex enum('F', 'M')
#birth_year unsigned smallint
#birth_month unsigned tinyint
#birth_day unsined tinyint
#school_type enum('P', 'S', 'H', 'T', 'J', 'O')分别指：小学、中学、大学、中专、大专、其他
#school_name varchar(40)
#school_grade unsigned tinyint
#建立表的sql语句:
"""create table baseInfo (uName varchar(15) not null, realName varchar(16), sex enum('F', 'M'), 
birthYear int(6) unsigned, birthMonth int(4) unsigned , birthDay int(4) unsigned , 
school_type enum('P', 'S', 'H', 'T', 'J', 'O'), school_name varchar(40), school_grade int(4) unsigned
 , foreign key(uName) references user(uName))"""

def save(u_name, r_name, sex, birth_year, birth_month, birth_day, 
	school_type, school_name, school_grade):
	"""保存用户的基本信息"""
	if database.is_exist('select * from baseInfo where uName = "%s" ' % u_name):
		database.query("""update baseInfo set realName = '%s', sex = '%s', birthYear = %d, birthMonth = %d,
			birthDay = %d, school_type='%c', school_name = '%s', school_grade = %d where uName = '%s'""" %
			(r_name, sex, birth_year, birth_month, birth_day, school_type, school_name, school_grade, u_name))
	else:
		database.query("""insert into baseInfo values('%s', '%s', '%c', %d, %d, %d, '%s', '%s', %d) """ % 
		(u_name, r_name, sex, birth_year, birth_month, birth_day, school_type, school_name, school_grade))

def getInfo(u_name):
	"""获取用户信息"""
	m = database.execute("select * from baseInfo where uName = '%s'" % u_name)
	if m:
		return m.fetchone()
	return ()


def getUser(r_name):
	"""通过真实姓名获得好友信息列表"""
	m = database.execute("select * from baseInfo where realName='%s'" % r_name)
	m = list(m.fetchall())
	return m








