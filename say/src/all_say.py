#encoding:utf-8
#返回用户请求的所有的说说号的json文件
#json格式:
#发生错误的情况
#{"error" : "Y", "info" : "some-error-info"}
#未发生错误
#{"error" : "N", "sayIds" : [id1, id2, ....]}

from mosquito.database import says, session
from django.http import HttpResponse

def all_say(request):
	"""获取所有的说说的ID"""
	u_name = session.has_login(request)
	#用户还没有登录，返回错误信息
	if not u_name:
		ret = "{'error' : 'Y', 'info' : '请先登录'}"
		return HttpResponse(ret)
	#合法用户，返回ID
	sayIds = says.get_all_sayId(u_name)
	ret = "{'error' : 'N', 'sayIds' : %s}" % sayIds.__repr__()
	return HttpResponse(ret)