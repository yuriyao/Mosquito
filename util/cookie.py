#encoding:utf-8
from generate import generate_sessionKey, generate_sessionId
from mosquito.database import session

#设置会话的cookie
def set_cookie(reponse, u_name=''):
	session_key = generate_sessionKey()
	session_id = generate_sessionId()
	#存储到数据库
	session.insert(session_id, session_key, u_name)
	#设置cookie
	reponse.set_cookie(session.SESSION_KEY, session_key)
	reponse.set_cookie(session.SESSION_ID, session_id)

def del_cookie(reponse):
	"""删除cookie"""
	reponse.set_cookie(session.SESSION_KEY, '')
	reponse.set_cookie(session.SESSION_ID, '')

