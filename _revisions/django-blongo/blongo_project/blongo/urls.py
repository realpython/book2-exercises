from django.conf.urls import url
from blongo import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
]
