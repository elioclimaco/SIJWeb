# -*- coding: utf-8 -*-

from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView
from django.utils import simplejson
from SIJWeb.settings import *

import xml.dom.minidom


class Prueba(TemplateView):
    template_name = 'depositos/index.html'


class Expedientes(TemplateView):
    template_name = 'depositos/listar.html'