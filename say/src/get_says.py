#encoding:utf-8
#请求参数:一组以,分隔的说说号
#返回json数据
#没有错误
#{'error' : 'N', 'says' : [{'sayId' : sayId1, 'sayText' : 'text1', 'time' : 'time1'}, ...]}
#如果发生错误
#{'error' : 'Y', 'info' : 'some-error-info'}


from mosquito.database import says, session
from django.http import HttpResponse

def get_says(request):
	"""获得一组说说"""
	u_name = session.has_login(request)
	if not u_name:
		return HttpResponse("{'error' : 'Y', 'info' : '请先登录'}")

	if request.method == 'GET':
		if 'sayIDs' in request.GET:
			sayIDs = request.GET['sayIDs']
			sayIDs = sayIDs.split(',')
			ret = "{'error' : 'N', 'says' : ["
			for i in range(len(sayIDs)):
				#只能是数字
				if sayIDs[i].isdigit():
					sayIDs[i] = int(sayIDs[i])
					#验证权限
					if says.is_author(sayIDs[i], u_name):
						res = says.get_text_and_time(sayIDs[i])
						if res:
							#对单引号进行转义
							sayText = res[0].replace('\'', '`')
							ret += "{'sayId' : %d, 'sayText' : '%s', 'time' : '%s'}," % (sayIDs[i], sayText, res[1])
			ret += "]}"
			return HttpResponse(ret)
	return HttpResponse("{'error' : 'Y', 'info' : '未定义错误'}")


