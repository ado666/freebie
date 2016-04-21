from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from fuser.models import User, UserFavorites
import datetime
import json

# Create your views here.


def update_location(request):
    print(request.POST)
    lng = request.POST['lng'][0]
    lat = request.POST['lat'][0]
    user = request.POST['user'][0]

    return HttpResponse(json.dumps({}), content_type = "application/json")

def hello(request):
    uuid = request.POST['uuid']
    token = request.POST['token']

    try:
        user = User.objects.get(uuid=uuid)
    except User.DoesNotExist:
        user = None

    if user is None:
        user = User()
        user.uuid = uuid
        user.token = token

    user.last_login = datetime.datetime.now()
    user.last_send = datetime.datetime.min
    user.current_lat = 0
    user.current_lng = 0

    user.save()

    return HttpResponse(json.dumps({'user': user.id}), content_type = "application/json")

def get_favorites(request):
    uuid = request.POST['uuid']
    token = request.POST['push_id']

    try:
        user = User.objects.get(uuid=uuid)
    except User.DoesNotExist:
        user = None

    if not user:
        return

    favorites = UserFavorites.objects.filter(user=user)
    data = [o.json() for o in favorites.all()]

    return HttpResponse(json.dumps({'favorites': data}), content_type = "application/json")
