from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from flocation.models import Location
from fuser.models import User
import datetime

import json

# Create your views here.

def update_location(request):
    lng = request.POST['lng']
    lat = request.POST['lat']
    user = request.POST['user']

    try:
        u = User.objects.get(pk=user)
    except:
        u = None

    if u is None:
        return HttpResponse(json.dumps({}), content_type = "application/json")
    
    l = Location()
    l.lng = lng
    l.lat = lat
    l.user = u
    l.time = datetime.datetime.now()

    u.current_lng = lng
    u.current_lat = lat

    l.save()
    u.save()

    return HttpResponse(json.dumps({}), content_type = "application/json")
