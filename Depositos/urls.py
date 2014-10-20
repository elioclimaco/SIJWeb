# -*- coding: utf-8 -*-

from django.conf.urls import url, patterns
from .views import *

urlpatterns = patterns('',
    # Prueba
    url(r'^prueba/$', Prueba.as_view(), name='Prueba'),

    # Expedientes
    url(r'^expedientes/$', Expedientes.as_view(), name='Expedientes')
)
