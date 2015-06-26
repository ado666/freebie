#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from fcompany.models import Company

# Create your views here.
def index(request):
    if request.user.is_authenticated():
        companies = Company.objects.all()
        return render_to_response('index.html', {'user': request.user, 'companies': companies})
    else:
        users = User.objects.all()
        return render_to_response('login.html', {'users': users})

def login(request):
    u = request.GET.get('username')
    p = request.GET.get('password')

    user = authenticate(username=u, password=p)
    if user is not None:
        auth_login(request, user)

    return HttpResponse('/')

def logout(request):
    auth_logout(request)
    return HttpResponse('/')