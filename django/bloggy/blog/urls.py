from django.conf.urls import patterns, include, url
from blog import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    # url(r'^(?P<post_id>\d+)/$', views.post, name='post'),
    url(r'^(?P<post_name>\w+)/$', views.post, name='post'),
)