#!/usr/bin/env python2.6
#encoding:utf-8
import KVS

#init的type值
#第一次启动
INIT_TYPE_CREATE = 1
#重新启动，加载保存的数据
INIT_TYPE_LOAD = 0

#初始化kvs系统
def kvs_init(disk_file_path, IMAGE_file_path, log_file_path, 
		init_type = INIT_TYPE_CREATE, buffer_sleep_time = 1, 
		buffer_horizon_size = 10, buffer_size = 100 * 1024 * 1024):
	return KVS.kvs_init(init_type, disk_file_path, IMAGE_file_path, log_file_path, 
			buffer_sleep_time, buffer_horizon_size, buffer_size)

#存储key/value值
def kvs_put(key, value):
	return KVS.kvs_put(key, value)

#获取key对应的value
def kvs_get(key):
	return KVS.kvs_get(key)

#删除key对应的key/value
def kvs_delete(key):
	return KVS.kvs_delete(key)

#退出kvs系统
def kvs_exit():
	return KVS.kvs_exit()


