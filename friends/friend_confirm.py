#encoding:utf-8
#用户对好友请求的处理
#同意或者拒绝
#请求方式:GET
#参数
#1、type:agree(同意), disagree(拒绝)
#2、friendFrom
#返回处理结果

from mosquito.database import session, add_friend, friends
from django.http import HttpResponse

def friend_confirm(request):
	u_name = session.has_login(request)
	if not u_name:
		return HttpResponse('请先登陆')
	if request.method == 'GET':
		if 'type' in request.GET and 'friendFrom' in request.GET:
			confirm_type = request.GET['type']
			friendFrom = request.GET['friendFrom']
			if confirm_type == 'disagree':
				add_friend.delete(friendFrom, u_name)
				return HttpResponse('确认成功')
			if add_friend.confirm(friendFrom, u_name):
				friends.save(friendFrom, u_name)
				return HttpResponse('确认成功')
	return HttpResponse('')

