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
