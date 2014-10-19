from django.conf.urls import patterns,url
from bbs import views

urlpatterns = patterns('',
    url(r'^$',views.index,name='index'),
    url(r'^p/(?P<page>\d+)/$',views.index,name='index'),
    url(r'^post_thread/$',views.post_thread,name='post_thread'),
    url(r'^t/(?P<thread_id>\d+)/$',views.thread,name='thread'),
    url(r'^t/(?P<thread_id>\d+)/send_comment/$',views.send_comment,name='send_comment'),
)
