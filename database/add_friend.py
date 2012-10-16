#encoding:utf-8
#数据库
#addFriend
#friendFrom varchar(15)
#friendTo varchar(15)
#state enum(0, 1)分别指未确认，已确认
"""create table addFriend(friendFrom varchar(15) not null, friendTo varchar(15) not null, state enum('0', '1') not null, 
	foreign key(friendFrom) references user(uName), foreign key(friendTo) references user(uName));"""

from database import database

def is_exist(friendFrom, friendTo):
	"""相应的表项是否已经存在"""
	return database.is_exist("select * from addFriend where friendFrom = '%s' and friendTo = '%s'" 
		% (friendFrom, friendTo))

def is_not_confirm(friendFrom, friendTo):
	"""相应的表项存在但未确认"""
	return database.is_exist("select * from addFriend where friendFrom = '%s' and friendTo = '%s' and state = '0'" 
		% (friendFrom, friendTo))

def delete(friendFrom, friendTo):
	"""删除相应的表项"""
	database.query("delete from addFriend where friendFrom = '%s' and friendTo = '%s' "
		% (friendFrom, friendTo))

def add_friend(friendFrom, friendTo):
	"""添加好友,等待确认"""
	if not is_exist(friendFrom, friendTo):
		database.query("insert into addFriend values('%s', '%s', '0')" % (friendFrom, friendTo))

def confirm(friendFrom, friendTo):
	"""好友确认"""
	if is_not_confirm(friendFrom, friendTo):
		database.query("update addFriend set state = '1' where friendFrom = '%s' and friendTo = '%s' " 
		% (friendFrom, friendTo))
		return True
	return False

def getAllRequest(u_name):
	"""获得所有好友请求的列表,返回用户名和真实姓名"""
	m = database.execute("""select uName, realName from baseInfo where uName in 
		(select friendFrom from addFriend where friendTo = '%s' and state='0') """ % u_name)
	if m:
		result = list(m.fetchall())
		return result
	return m





