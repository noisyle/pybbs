from django.conf.urls import patterns, include, url
from django.contrib import admin
from mysite.settings import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^upload/(?P<path>.*)', 'django.views.static.serve', {'document_root': MEDIA_ROOT}),
    url(r'^bbs/', include('bbs.urls', namespace="bbs")),
)
