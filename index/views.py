#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def main(request):
    post_data = [{address: 'Ð³Ð¾Ð´+ÐÐ¾ÑÐºÐ²Ð°,+ÐÐ¾ÑÐºÐ²Ð°,+Ð£ÑÐ°Ð»ÑÑÐºÐ°Ñ+ÑÐ»Ð¸ÑÐ°'}]     # a sequence of two element tuples
    result = urllib2.urlopen('http://example.com', urllib.urlencode(post_data))
    content = result.read()
    
    return HttpResponse("Hello, world. You're at the polls index.")
