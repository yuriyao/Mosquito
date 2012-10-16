#encoding:utf-8

from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from mosquito.database import user, session
from mosquito.util import cookie
import re

CHAR_OR_NUM = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_'

class Log_User:
	def __init__(self, u_name, u_pwd):
		self.u_name = u_name
		self.u_pwd = u_pwd

	def u_name_valid(self):
		"""验证用户名是否合法,只是字面上的"""
		u_name_len = len(self.u_name)
		for i in range(u_name_len):
			if not self.u_name[i] in CHAR_OR_NUM:
				return False
		return True

	def u_pwd_valid(self):
		"""验证密码的合法性,只是字面上的"""
		pwd_pattern = '^[0-9a-zA-Z_]+$'
		if re.match(pwd_pattern, self.u_pwd):
			return True
		return False

	def validate(self):
		"""验证登录信息是否合法"""
		if self.u_name_valid() and self.u_pwd_valid():
			if user.is_valid(self.u_name, self.u_pwd):
				return True
		return False


def login(request):
	"""处理用户登录验证"""
	#如果用户已经登录
	if session.has_login(request):
		return HttpResponseRedirect('/mainpage/')
	u_name = ''
	u_pwd = ''
	error = ''
	if 'u_name' in request.POST and 'u_pwd' in request.POST:
		u_name = request.POST['u_name']
		u_pwd = request.POST['u_pwd']
		login = Log_User(u_name, u_pwd)
		if login.validate():
			response = HttpResponseRedirect('/mainpage/')
			cookie.set_cookie(response, login.u_name)
			return response
		else:
			error = '用户名或者密码有误，请重新登录'
	return render_to_response('login.html', {'error' : error, 'u_name' : u_name, 'u_pwd' : u_pwd})

