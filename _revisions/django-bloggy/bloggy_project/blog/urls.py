from django.conf.urls import url
from blog import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add_post/', views.add_post, name='add_post'),
    url(r'^(?P<slug>[\w|\-]+)/$', views.post, name='post'),
]
