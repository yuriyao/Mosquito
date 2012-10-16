#encoding:utf-8
#安全验证模块
import re

DANGER_CHARS = "<>#-/*\\';"
U_NAME_MAX = 15
U_NAME_MIN = 5


def contain_danger(str):
	"""检测是否包含不安全的字符"""
	str_len = len(str)
	for i in range(str_len):
		if str[i] in DANGER_CHARS:
			return True
	return False

def is_valid_u_name(u_name):
	"""验证用户名是否合法"""
	if len(u_name) > U_NAME_MAX or len(u_name) < U_NAME_MIN:
		return False
	patten = '^\w+$'
	if re.match(patten, u_name):
		return True
	return False

