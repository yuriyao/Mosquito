#encoding:utf-8
#处理用户会话的数据库部分
#会话数据库由四项组成:
#session_id 会话id 
#session_key 会话key
#u_name 用户的name
#last_active 最后一次活跃的时间

from database import database
from mosquito.util import generate
#from mosquito.util import cookie
from time import strftime, strptime
from datetime import datetime

SESSION_KEY = 'sessionKey'
SESSION_ID = 'sessionID'
#cookie的生存时间(不活动的时间)12小时
COOKIE_LIFE = 43200

def has_login(request):
	"""通过cookie来确认用户是否已经登录,返回会话的用户名"""
	if SESSION_KEY in request.COOKIES and SESSION_ID in request.COOKIES:
		session_key = request.COOKIES[SESSION_KEY]
		session_id = request.COOKIES[SESSION_ID]
		if generate.session_key_validate(session_key) and generate.session_id_validate(session_id):
			c = database.execute("select uName, lastActive from session "
					"where sessionId = '%s' and sessionKey = '%s'" % (session_id, session_key))
			if c:
				u_name, lastActive= c.fetchone()
				delta = datetime.now() - lastActive
				if delta.seconds <= COOKIE_LIFE:
					return u_name
	return ''



def insert(session_id, session_key, u_name):
	"""将会话信息保存到数据库"""
	time = strftime('%Y-%m-%d %H:%M:%S')
	database.query("insert into session (sessionId, sessionKey, uName, lastActive)"
	 "values('%s', '%s', '%s', '%s')" % (session_id, session_key, u_name, time))



