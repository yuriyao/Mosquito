#encoding:utf-8

from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from mosquito.database import says, session

def say(request):
	u_name = session.has_login(request)
	if not u_name:
		return HttpResponseRedirect('/login/')
	return render_to_response('say.html')