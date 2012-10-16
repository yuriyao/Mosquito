#encoding: utf-8
#存储用户发布的说说
#用户的说说必然是由ajax post过来的

from mosquito.database import says, session
from django.http import HttpResponse, HttpResponseRedirect

def public_say(request):
	"""存储用户的说说"""
	u_name = session.has_login(request)
	if not u_name:
		return HttpResponseRedirect('/login/')
	if request.method == 'POST':
		if 'say' in request.POST:
			says.save(u_name, request.POST['say'])
			return HttpResponse('说说发布成功')
	return HttpResponse('你懂的')
