#encoding:utf-8
#说说数据表says
#sayId:int(15) primary key
#author:varchar(15) foreign key
#text:varchar(150)
#time:datetime not null
"""" create table say(sayId int(15) primary key AUTO_INCREMENT, author varchar(15) not null, 
		text varchar(150), time datetime not null, foreign key(author) references user(uName)); """

from database import database
import time

TEXT_MAX = 150

def save(author, context):
	"""保存说说"""
	#去掉单引号
	context = context.replace('\'', '\\\'')
	now = time.strftime('%Y-%m-%d %H:%M:%S')
	database.query("insert into say(author, text, time) values('%s', '%s', '%s')" % (author, context, now))

def get_all_sayId(u_name):
	"""获得用户所有的sayId的列表"""
	m = database.execute("select sayId from say where author = '%s' order by sayId desc" % u_name)
	sayIds = list(m.fetchall())
	for i in range(len(sayIds)):
		sayIds[i] = int(sayIds[i][0])
	return sayIds

def get_text_and_time(sayId):
	"""获得一条说说的内容和时间"""
	m = database.execute("select text, time from say where sayId = %d" % sayId)
	result = ('', '')
	if m:
		result = m.fetchone()
	return result

def get_text(sayId):
	"""获取一条说说的内容"""
	m = database.execute('select text from say where sayId = %d' % sayId)
	if m:
		m = m.fetchone()
	return m

def delete(sayId):
	"""删除一条说说"""
	database.query("delete from say where sayId = %d" % sayId)

def is_author(sayId, u_name):
	"""验证u_name是否是sayId说说的作者"""
	return database.is_exist("select sayId from say where sayId = %d and author = '%s'" % (sayId, u_name))

def get_last_one_text_time(u_name):
	"""获得最新的说说的内容和时间"""
	m = database.execute("select sayId, text, time from say where author = '%s' order by sayId desc" % u_name)
	if m:
		return m.fetchone()
	return m