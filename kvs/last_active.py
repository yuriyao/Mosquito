#encoding:utf-8
#获得和设置用户最近的活动情况
#在这个kvs系统中，存储两个键值对
#key:用户名
#value用户最后的活动时间

import kvs
import time

def active_init():
	return kvs.kvs_init('disk_active', 'image_active', 'log_active', init_type = kvs.INIT_TYPE_LOAD)

#获得用户最近的请求时间，如果其不存在，则设置其时间为一周前
def get_last_active(u_name):
	"""获得用户最近的请求时间"""
	active_time = kvs.kvs_get(u_name)
	if not active_time:
		pass 
	return active_time

#
def set_last_active(u_name):
	"""设置用户最后的请求时间"""
	now = time.strftime('%Y-%m-%d %H:%M:%S')
	kvs.kvs_delete(u_name)
	kvs.kvs_put(u_name, now)

#释放系统资源
def active_release():
	kvs.kvs_exit()
