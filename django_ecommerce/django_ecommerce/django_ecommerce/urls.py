"""django_ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from main import views as main_views
from contact import views as contact_views
from payments import views as payment_views

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', main_views.index, name='home'),
    url(r'^pages/', include('django.contrib.flatpages.urls')),
    url(r'^contact/', contact_views.contact, name='contact'),
    # user registration/authentication
    url(r'^sign_in$', payment_views.sign_in, name='sign_in'),
    url(r'^sign_out$', payment_views.sign_out, name='sign_out'),
    url(r'^register$', payment_views.register, name='register'),
    url(r'^edit$', payment_views.edit, name='edit'),
]
