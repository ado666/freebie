from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from fuser.models import User, UserFavorites
from fcompany.models import Company
from foffer.models import OfferCategory, CategoryToUser
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

def favorite_delete(request):
    uuid = request.POST['uuid']
    cid = request.POST['company_id']

    try:
        user = User.objects.get(uuid=uuid)
    except User.DoesNotExist:
        user = None

    if not user:
        return HttpResponse(json.dumps({'result': "not_found_user"}), content_type = "application/json")

    company = Company.objects.get(pk=cid)
    favorite = UserFavorites.objects.get(user=user, company=company)

    favorite.delete()

    return HttpResponse(json.dumps({'result': "ok"}), content_type = "application/json")

def get(request):
    uuid = request.POST['uuid']

    try:
        user = User.objects.get(uuid=uuid)
    except User.DoesNotExist:
        user = None

    if not user:
        return

    categories = OfferCategory.objects
    category_to_user = CategoryToUser.objects.filter(user=user)

    categories = [o.json() for o in categories.all()]
    categories_config = {}
    for cc in category_to_user:
        item = cc.json()
        categories_config[item['category_id']] = item['value']

    print(categories_config)
    return HttpResponse(json.dumps({
        'result': "ok",
        'data': {
            'categories': categories,
            'categories_config': categories_config,
            'favorite_companies': {}
        }
    }), content_type = "application/json")

def category_update(request):
    uuid = request.POST['uuid']
    category_id = request.POST['category_id']
    value = request.POST['value']

    return HttpResponse(json.dumps({'result': "ok"}), content_type = "application/json")