#encoding:utf-8

from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
import re
from mosquito.util import cookie
from mosquito.database import session, user

#处理用户注册表单
class Form:
	def __init__(self, u_name='', u_pwd='', u_confirm='', u_email=''):
		self.u_name = u_name
		self.u_pwd = u_pwd
		self.u_confirm = u_confirm
		self.u_email = u_email
	def valid(self):
		#验证用户名是否合法
		#用户名必须是字母和数字和下划线,且长度不大于15,且不小于5
		#其实如果用户正常使用蚊蚊网，是不需要这么严格的检查的
		#但是可能会有恶意用户通过非正常途径post数据
		result = True
		u_name_len = len(self.u_name)
		#验证用户名长度
		if u_name_len > 15:
			result = False
			self.u_name_error = '用户名过长(不应长于15个字符)'
		elif u_name_len < 5:
			result = False
			self.u_name_error = '用户名过短(不应短于5个字符)'
		else:
			#验证用户名的字符
			for i in range(u_name_len):
				if not is_num_or_char(self.u_name[i]):
					result = False
					self.u_name_error = '用户名中包含非法字符'
		#验证用户名是否存在
		if result:
			 if user.u_name_logined(self.u_name):
			 	result = False
			 	self.u_name_error = '用户名已经被注册'

		#验证两次密码是否相同
		if self.u_pwd != self.u_confirm:
			result = False
			self.u_pwd_error = '两次密码不相同'
		else:
			u_pwd_len = len(self.u_pwd)
			#验证密码长度,密码长度应该不小于5且不大于30
			if u_pwd_len < 5:
				result = False
				self.u_pwd_error = '密码长度过短(不应小于5个字符)'
			elif u_pwd_len > 30:
				result = False
				self.u_pwd_error = '密码长度过长(不应长于30个字符)'
			#验证密码的字符是否合法
			else:
				for i in range(u_pwd_len):
					if not is_num_or_char(self.u_pwd[i]):
						result = False
						self.u_pwd_error = '密码中含有非法字符'

		#验证e-mail是否合法
		if not is_email_validate(self.u_email):
			result = False
			self.u_email_error = 'e-mail地址不合法'
		elif len(self.u_email) > 40:
			result = False
			self.u_email_error = 'e-mail地址过长(不应长于40个字符)'
		#验证是否该e-mail地址已被注册
		elif user.u_email_logined(self.u_email):
			result = False
			self.u_email_error = 'e-mail地址已被注册'
		return result

	def save(self):
		"""保存表单信息"""
		user.insert(self.u_name, self.u_pwd, self.u_email)


#检查ch是否是数字，字母和下划线
def is_num_or_char(ch):
	if len(ch) > 1:
		return False
	if ((ord(ch) >= ord('0') and ord(ch) <= ord('9'))
	 		or	(ord(ch) <= ord('z') and ord(ch) >= ord('a'))
	 		or (ord(ch) <= ord('Z') and ord(ch) >= ord('A')) 
	 		or (ord(ch) == ord('_'))):
		return True
	return False

#检查是否是合法的e-mail地址
def is_email_validate(e_mail):
	#e-mail地址的正则表达式
	email_patten = '\w+@(\w+\.)*\w+\.\w+$'
	m = re.match(email_patten, e_mail)
	if m:
		return True
	return False

#响应用户的注册
def register(request):
	#如果用户已经登录
	if session.has_login(request):
		return HttpResponseRedirect('/mainpage/')
	form = Form()
	if request.method == 'POST':
		if ('u_name' in request.POST 
			and 'u_pwd' in request.POST 
			and 'u_confirm' in request.POST
			and 'u_email' in request.POST):
			form = Form(request.POST['u_name'], request.POST['u_pwd'], 
				request.POST['u_confirm'], request.POST['u_email'])
			if form.valid():
				form.save()
				response = HttpResponseRedirect('/mainpage/')
				cookie.set_cookie(response, request.POST['u_name'])
				return response
	return render_to_response('register.html', {'user' : form})


