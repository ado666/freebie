#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render
import urllib2

# Create your views here.
def main(request):
    post_data = [{'address': 'город Москва, Москва, Уральская улица'}]     # a sequence of two element tuples
    result = urllib2.urlopen('http://example.com', urllib2.urlencode(post_data))
    content = result.read()
    
    return HttpResponse("Hello, world. You're at the polls index."+content)
