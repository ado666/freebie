#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render
import urllib2, urllib

# Create your views here.
def main(request):
    post_data = {'address': u'город+Москва,+Москва,+Уральская+улица'}     # a sequence of two element tuples
    result = urllib2.urlopen('https://maps.googleapis.com/maps/api/geocode/json', urllib.urlencode(post_data))
    content = result.read()

    print urllib.urlencode(post_data)
    
    return HttpResponse("Hello, world. You're at the polls index."+content)
