# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SIJWeb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # Depósitos.
    url(r'depositos/', include('Depositos.urls', namespace='Depositos')),

    # Admin.
    url(r'^admin/', include(admin.site.urls)),
)
