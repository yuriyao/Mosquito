#encoding:utf-8
#表名:
#friend1: varchar(15) 
#friend2: varchar(15)
#在存储时friend1必须是"小于"friend2
"""create table friends(friend1 varchar(15) not null, friend2 varchar(15) not null, 
	foreign key(friend1) references user(uName), foreign key(friend2) references user(uName))"""

from database import database

def is_friend(friend1, friend2):
	"""检查两个用户是否是好友关系"""
	tmp = friend1
	if friend1 > friend2:
		tmp = friend1
		friend1 = friend2
		friend2 = tmp
	return database.is_exist("""select * from friends where (friend1 = '%s' and friend2 = '%s') """ % (friend1, friend2))

def save(friend1, friend2):
	"""保存好友关系"""
	if not is_friend(friend1, friend2):
		if friend1 > friend2:
			tmp = friend1
			friend1 = friend2
			friend2 = tmp
		database.query("""insert into friends values('%s', '%s')""" % (friend1, friend2))

def get_friends(u_name):
	"""获取所有好友用户名的列表"""
	cur = database.execute("select friend1 from friends where friend2 = '%s' " % u_name)
	friends =  cur.fetchall()
	friends = list(friends)
	for i in range(len(friends)):
		friends[i] = friends[i][0]

	cur = database.execute("select friend2 from friends where friend1 = '%s' " % u_name)
	friends2 = cur.fetchall()
	friends2 = list(friends2)
	for i in range(len(friends2)):
		friends2[i] = friends2[i][0]
	friends += friends2
	return friends

def delete(friend1, friend2):
	"""删除好友关系"""
	tmp = friend1
	if friend1 > friend2:
		friend1 = friend2
		friend2 = tmp
	database.query('delete from friends where friend1 = "%s" and friend2 = "%s"' % (friend1, friend2))




