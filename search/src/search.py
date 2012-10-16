#encoding:utf-8

from django.http import HttpResponse
from mosquito.util import security
from mosquito.database import base_info
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

SCHOOL_NAME = 7
U_NAME = 0

def search(request):
	"""返回用户名查询信息的json"""
	result = '[]'
	if request.method == 'GET':
		if 'search' in request.GET:
			#检测用户的查询请求是否是安全的
			if not security.contain_danger(request.GET['search']):
				li = base_info.getUser(request.GET['search'])
				#构造规范的json数据
				if li:
					result = '['
					for user in li:
						result += '{"img_src":"/main_page_css/1.jpg", "school_name" : "%s", "friend_uname" : "%s"},' % (
							user[SCHOOL_NAME], user[U_NAME])
					result += ']'
	return HttpResponse(result)

