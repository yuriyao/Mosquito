#encoding:utf-8

from mosquito.util import cookie
from django.http import HttpResponseRedirect

def logout(request):
	"""让用户登出——删除cookie"""
	response = HttpResponseRedirect('/login/')
	cookie.del_cookie(response)
	return response