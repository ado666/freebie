from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from flocation.models import Location
from fuser.models import User as Fuser
import datetime

import json

# Create your views here.

def update_location(request):
    lng = request.POST['lng']
    lat = request.POST['lat']
    uuid = request.POST.get('uuid', None)

    try:
        user = Fuser.objects.get(uuid=uuid)
    except Fuser.DoesNotExist:
        user = None

    if user is None:
        return HttpResponse(json.dumps({}), content_type = "application/json")
    
    l = Location()
    l.lng = lng
    l.lat = lat
    l.user = user
    l.time = datetime.datetime.now()

    user.current_lng = lng
    user.current_lat = lat

    l.save()
    user.save()

    return HttpResponse(json.dumps({}), content_type = "application/json")
