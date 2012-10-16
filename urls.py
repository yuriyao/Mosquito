#encoding:utf-8
from django.conf.urls.defaults import *
import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

#指定css,js,jquery的路径
urlpatterns = patterns('',
	(r'^main_page_css/(?P<path>.*)$', 'django.views.static.serve', {'document_root' : 'mainpage/main_page_css'}),
	(r'main_page_js/(?P<path>.*)$', 'django.views.static.serve', {'document_root' : 'mainpage/main_page_js'}),
	(r'global/(?P<path>.*)$', 'django.views.static.serve', {'document_root' : 'global'}),
    (r'user_css/(?P<path>.*)$', 'django.views.static.serve', {'document_root' : 'user/user_css'}),
    (r'user_js/(?P<path>.*)$', 'django.views.static.serve', {'document_root' : 'user/user_js'}),
    (r'info_css/(?P<path>.*)$', 'django.views.static.serve', {'document_root' : 'info/info_css'}),
    (r'info_js/(?P<path>.*)$', 'django.views.static.serve', {'document_root' : 'info/info_js'}),
    (r'search_css/(?P<path>.*)$', 'django.views.static.serve', {'document_root' : 'search/search_css'}),
    (r'search_js/(?P<path>.*)$', 'django.views.static.serve', {'document_root' : 'search/search_js'}),
    (r'say_css/(?P<path>.*)$', 'django.views.static.serve', {'document_root' : 'say/say_css'}),
    (r'say_js/(?P<path>.*)$', 'django.views.static.serve', {'document_root' : 'say/say_js'}),
    # Example:
    # (r'^mosquito/', include('mosquito.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('mainpage.src',
	('^mainpage/$', 'mainpage.mainpage'),

)

urlpatterns += patterns('user.src',
    ('^register/$', 'register.register'),
    ('^logout/$', 'logout.logout'),
    ('^login/$', 'login.login'),
    ('^$', 'login.login'),
)

urlpatterns += patterns('info.src',
    ('^info/$', 'info.info'),
)

urlpatterns += patterns('search.src',
    ('^search/$', 'search.search'),
)

urlpatterns += patterns('friends',
    ('^add_friend/$', 'add_friends.add_friends'),
    ('^get_friend_request/$', 'friend_request.friend_request'),
    ('^friend_confirm/$', 'friend_confirm.friend_confirm'),
)

urlpatterns += patterns('say.src',
    ('^public_say/$', 'public_say.public_say'),
    ('^say/$', 'say.say'),
    ('^all_say/$', 'all_say.all_say'),
    ('^get_say/$', 'get_say.get_say'),
    ('^get_says/$', 'get_says.get_says'),
    ('^get_last_one/$', 'get_say.get_last_one'),
)