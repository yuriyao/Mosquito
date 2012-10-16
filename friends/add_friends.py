#encoding:utf-8

from mosquito.database import friends, session, add_friend
from django.http import HttpResponse
from mosquito.util import security

def add_friends(request):
	"""添加好友请求"""
	u_name = session.has_login(request)
	if not u_name:
		return HttpResponse('请先登录')
	if request.method == 'POST':
		if 'friendName' in request.POST:
			friendTo = request.POST['friendName']
			if security.is_valid_u_name(u_name):
				if friends.is_friend(u_name, friendTo):
					return HttpResponse('已是好友')
				else:
					add_friend.add_friend(u_name, friendTo)
					return HttpResponse('请求已发出')
	return HttpResponse('你懂的')
