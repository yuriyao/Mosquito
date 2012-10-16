#encoding:utf-8

from django.http import HttpResponse
from mosquito.database import says,session

def get_say(request):
	u_name = session.has_login(request)
	if not u_name:
		return HttpResponse('')
	if request.method == 'GET':
		if 'sayID' in request.GET:
			sayID = request.GET['sayID']
			#sayID必须是数字
			if sayID.isdigit():
				sayID = int(sayID)
				#请求是否权限允许
				if says.is_author(sayID, u_name):
					ret = says.get_text(sayID)
					return HttpResponse(ret)
	return HttpResponse('')

def get_last_one(request):
	u_name = session.has_login(request)
	if not u_name:
		return HttpResponse('')
	last_one = says.get_last_one_text_time(u_name)
	if last_one:
		sayText = last_one[1].replace('\'', '`')
		ret = "{'sayId' : %s, 'sayText' : '%s', 'time' : '%s'}" % (last_one[0], sayText, last_one[2])
		return HttpResponse(ret)
	return HttpResponse('')

