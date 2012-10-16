#encoding:utf-8
#用户好友请求信息的获取
#请求方式:GET
#参数:没有
#返回的json数据
#没有错误
#{'type' : 'FR', 'list' : [{'u_name' : 'u_name1', 'r_name' : 'r_name1'}, ...]}
#出错
#{'type' : 'errorno', 'info' : 'error-info'}
#出错号详见util/error

from mosquito.database import session, add_friend
from mosquito.util import error
from django.http import HttpResponse

def friend_request(request):
	u_name = session.has_login(request)
	if not u_name:
		return HttpResponse("{'type' : '%d', 'info' : '请先登陆'}" % error.NO_LOGIN)
	if request.method == 'GET':
		ret = "{'type' : 'FR', 'list' : ["
		li = add_friend.getAllRequest(u_name)
		if li:
			for user in li:
				ret += "{'u_name' : '%s', 'r_name' : '%s'}," % user
		ret += "]}"
		return HttpResponse(ret)
	return HttpResponse("{'type' : '%d', 'info' : '未使用GET方式'}" % error.NO_GET_ERROR)


