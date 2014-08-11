from django.conf.urls import patterns, url
from blongo import views

urlpatterns = patterns('blongo.views',
    url(r'^$', views.index, name='index'),
)
