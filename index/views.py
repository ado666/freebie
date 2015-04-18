#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from django.shortcuts import render
import urllib2, urllib

# Create your views here.
def index(request):
    # post_data = {'address': 'asd'}     # a sequence of two element tuples
    # result = urllib2.urlopen('https://maps.googleapis.com/maps/api/geocode/json', urllib.urlencode(post_data))
    # content = result.read()
    # t = get_template('main.html')
    # t = template.Template('My name is {{ name }}.')
    # c = template.Context({'name': 'Adrian'})
    # return t.render()
    return render_to_response('main.html', {'users': ['msy', 'asd']})
    
    # return HttpResponse("Hello, world. You're at the polls index."+content)
