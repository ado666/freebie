from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from flocation.models import Location

import json

# Create your views here.

def update_location(request):
    lng = request.POST['lng'][0]
    lat = request.POST['lat'][0]
    user = request.POST['user'][0]
    
    l = Location()
    l.lng = lng
    l.lat = lat
    l.uuid = user
    print(l)
    l.save()

    return HttpResponse(json.dumps({}), content_type = "application/json")
