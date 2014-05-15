from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from settings import MEDIA_ROOT

urlpatterns = patterns('',
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('blog.urls')),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root':  MEDIA_ROOT}),
)
