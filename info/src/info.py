#encoding:utf-8
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from mosquito.database import session, base_info
from mosquito.util import security
import time

R_NAME_MAX = 16
SCHOOL_NAME_MAX = 40

#組成:學校種類的編號 : '存儲的類型枚舉值
SCHOOL_TYPE = {'1' : 'P' , '2' : 'S', '3' : 'H', '4' : 'T', '5' : 'J', '6' : 'O'}  
#
SCHOOL_GRADE = {'P': 7, 'S' : 8, 'H' : 7, 'T' : 6, 'J' : 6, 'O' : 0}

class User_Info:
	def __init__(self, u_name='', r_name='', sex='', birth_year='',
		 birth_month='', birth_day='', school_type='', 
		 school_name='', school_grade=''):
		self.u_name = u_name
		self.r_name = r_name
		self.sex = sex
		self.birth_year = birth_year
		self.birth_month = birth_month
		self.birth_day = birth_day
		self.school_type = school_type
		self.school_name = school_name
		self.school_grade = school_grade
		self.r_name_error = ''
		self.school_name_error = ''

	def is_validate(self):
		""" 是否是规范的"""
		result = True
		#验证用户名的合法性
		if len(self.r_name) > R_NAME_MAX:
			self.r_name_error = '用户名过长(不能大于6个中文字符)'
			result = False
		elif security.contain_danger(self.r_name):
			self.r_name_error = '用户名包含非法字符(你懂的)'
			result = False
		#验证用户学校名称的合法性
		if len(self.school_name) > SCHOOL_NAME_MAX:
			self.school_name_error = '学校名称过长'
			result = False
		elif security.contain_danger(self.school_name):
			self.school_name_error = '学校名称包含非法字符(你懂的)'
			result = False
		return result

	def save(self):
		"""保存用户的基本信息"""
		#规范化用户性别
		if(self.sex != 'F'):
			self.sex = 'M'
		#规范用户出生年份
		year_now = time.localtime().tm_year;
		self.birth_year = standardize(self.birth_year, 1900, year_now, 1992)
		#规范用户的出生月份
		self.birth_month = standardize(self.birth_month, 1, 12, 5)
		#规范用户出生日期
		#小月
		if(self.birth_month == 4 or self.birth_month == 6 
			or self.birth_month == 9 or self.birth_month == 11):
			self.birth_day = standardize(self.birth_day, 1, 30, 11)
		#2月
		elif(self.birth_month == 2):
			#闰年
			if (self.birth_year == self.birth_year // 4 * 4 
				and self.birth_year != self.birth_year // 100 * 100):
				self.birth_day = standardize(self.birth_day, 1, 29, 11)
			#平年
			else:
				self.birth_day = standardize(self.birth_day, 1, 28, 11)
		else:
			self.birth_day = standardize(self.birth_day, 1, 31, 11)
		#规范用户学校类型,默认是大学
		self.school_type = SCHOOL_TYPE.get(self.school_type, 'H')
		#规范学校年级数
		if self.school_type != 'O':
			self.school_grade = standardize(self.school_grade, 1, SCHOOL_GRADE[self.school_type], 1)
		else:
			self.school_grade = 0
		#存储到数据库
		base_info.save(self.u_name, self.r_name, self.sex, self.birth_year, self.birth_month, 
			self.birth_day, self.school_type, self.school_name, self.school_grade)

def standardize(str, min, max, default):
	"""数值字符进行规范化"""
	if str.isdigit():
		str = int(str, 10)
	else:
		str = default
	if str < min:
		str = min
	elif str > max:
		str = max
	return str



def info(request):
	"""相应用户信息查询和修改的请求"""
	u_name = session.has_login(request)
	if not u_name:
		return HttpResponseRedirect('/login/')
	year_to_now = range(1900, time.localtime().tm_year + 1)
	months = range(1, 13)
	days = range(1, 32)
	user_info = User_Info('', '', '', '', '', '', '', '', '')
	if request.method == 'POST':
		post = request.POST
		if ('r_name' in post and 'sex' in post and 'birth_year' in post
			and 'birth_month' in post and 'birth_day' in post 
			and 'school_type' in post and 'school' in post and 'grade' in post):
			r_name =  post['r_name']
			sex = post['sex']
			birth_year = post['birth_year']
			birth_month = post['birth_month']
			birth_day = post['birth_day']
			school_type = post['school_type']
			school_name = post['school']
			school_grade = post['grade']
			user_info = User_Info(u_name, r_name, sex, birth_year, birth_month, 
				birth_day, school_type, school_name, school_grade)
			if user_info.is_validate():
				user_info.save()
				return HttpResponse('信息修改成功')
		return HttpResponse(('信息修改失败,由于:%s %s' % (user_info.r_name_error, user_info.school_name_error)))
			#user_info = User_Info(u_name, r_name, sex, birth_year, birth_month, 
			#	birth_day, school_type, school_name, school_grade)
	else:
		info = base_info.getInfo(u_name)
		if info:
			user_info = User_Info(*info)
		else:
			user_info = User_Info()
		return render_to_response('info.html', {'year_to_now' : year_to_now, 'months' : months, 'days' : days, 'user' : user_info})



