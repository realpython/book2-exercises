from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^hello/$', 'hw.views.hello_view'),
    url(r'^$', 'hw.views.hello_view'),
    url(r'^better/$', 'hw.views.better'),
)
