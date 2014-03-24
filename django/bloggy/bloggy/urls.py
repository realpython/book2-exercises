from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from settings import  MEDIA_ROOT

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/$', 'blog.views.index'),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root':  MEDIA_ROOT}),
    url(r'^blog/(?P<post_id>\d+)/$', 'blog.views.post'),
)
