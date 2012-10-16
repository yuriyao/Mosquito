#encoding:utf-8
#负责产生一些随机序列
from random import randint, choice, sample
from time import localtime

CHARS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
HEX_NUM = '0123456789ABCDEF'
SESSION_ID_LEN = 27
SESSION_KEY_LEN = 20
#counter不是线程安全的
counter = 0;

def generate_char():
	"""随机产生一个大写或者小写字母"""
	return choice(CHARS)

def generate_hex():
	"""随机产生一个表示十六进制数的字符(大写)"""
	return choice(HEX_NUM)

def generate_sessionKey():
	"""随机生成一组长度为20的sessionKey"""
	#申请长度为20的列表
	result = range(SESSION_KEY_LEN)
	for i in range(SESSION_KEY_LEN):
		result[i] = choice(HEX_NUM)
	return ''.join(result)

#生成方法：
#12位随机十六进制数 + 10位时间相关的字符 + 5位累加数
def generate_sessionId():
	"""生成一组长度为27的sessionId,sessionId必须唯一"""
	result = range(SESSION_ID_LEN)
	now = localtime()
	#生成最高8位随机数
	for i in range(12):
		result[i] = choice(HEX_NUM)
	#生成10位时间相关的字符(05-11-18:21:31)
	result[12] = CHARS[now.tm_sec % 10]
	result[13] = CHARS[now.tm_sec / 10]
	result[14] = CHARS[now.tm_min % 10]
	result[15] = CHARS[now.tm_min / 10]
	result[16] = CHARS[now.tm_hour % 10]
	result[17] = CHARS[now.tm_hour / 10]
	result[18] = CHARS[now.tm_mday % 10]
	result[19] = CHARS[now.tm_mday / 10]
	result[20] = CHARS[now.tm_mon % 10]
	result[21] = CHARS[now.tm_mon / 10]
	#5位累加数
	global counter
	temp = counter
	counter += 1
	if counter >= 100000:
		counter = 0
	result[22] = CHARS[temp % 10 + 10]
	temp /= 10
	result[23] = CHARS[temp % 10 + 10]
	temp /= 10
	result[24] = CHARS[temp % 10 + 10]
	temp /= 10
	result[25] = CHARS[temp % 10 + 10]
	temp /= 10
	result[26] = CHARS[temp + 10]
	return ''.join(result)

def session_key_validate(session_key):
	"""验证session_key是否合法"""
	length = len(session_key)
	if length != SESSION_KEY_LEN:
		return False
	for i in range(length):
		if not (session_key[i] in HEX_NUM):
			return False
	return True

def  session_id_validate(session_id):
	"""验证session_id是否合法"""
	length = len(session_id)
	if length != SESSION_ID_LEN:
		return False
	for i in range(length):
		char_num = CHARS + HEX_NUM
		if not (session_id[i] in char_num):
			return False
	return True