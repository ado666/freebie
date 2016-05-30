# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from fuser.models import User as Fuser, UserFavorites
from django.conf import settings
from foffer.models import Offer, OfferCategory, CategoryToUser
from fcompany.models import Company
from faddress.models import Address
import datetime
import json
from PIL import Image



# Create your views here.
def save(request):
    oid     = request.POST.get('id')
    cid     = request.POST.get('cid')
    name    = request.POST.get('name')
    desc    = request.POST.get('desc')
    dist    = request.POST.get('dist')
    sdate   = request.POST.get('sdate')
    edate   = request.POST.get('edate')

    mo      = int(request.POST.get('mo'))
    tu      = int(request.POST.get('tu'))
    we      = int(request.POST.get('we'))
    th      = int(request.POST.get('th'))
    fr      = int(request.POST.get('fr'))
    sa      = int(request.POST.get('sa'))
    su      = int(request.POST.get('su'))

    url     = request.POST.get('img_url')

    stime   = request.POST.get('stime') + ':00'
    etime   = request.POST.get('etime') + ':00'

    lat     = request.POST.get('lat')
    lng     = request.POST.get('lng')
    cat     = request.POST.get('category')

    sdate   = datetime.datetime.strptime(sdate, "%d-%m-%Y").date()
    edate   = datetime.datetime.strptime(edate, "%d-%m-%Y").date()

    if oid:
        o = Offer.objects.get(pk=oid)
    else:
        o = Offer()
        o.user     = request.user

    company = Company.objects.get(pk=cid)

    o.company  = company
    o.name  = name
    o.desc  = desc
    o.dist  = dist
    o.date_start    = sdate
    o.date_end      = edate
    o.mo    = mo
    o.tu    = tu
    o.we    = we
    o.th    = th
    o.fr    = fr
    o.sa    = sa
    o.su    = su

    o.time_start    = stime
    o.time_end      = etime
    o.category      = OfferCategory.objects.get(pk=cat)

    if url == 'img/blank.png':
        o.icon = ''

    o.save()

    if request.FILES:
        file = request.FILES['file']
        path = settings.IMAGES_DIR + '/offers/' + request.user.username + str(o.id) + '.png'
        thumb_path = settings.IMAGES_DIR + '/pins/' + request.user.username + str(o.id) + '.png'
        fout = open(path,'w')
        fout.write(file.read())
        # print(file)
        # im = Image.open(file)
        # im.thumbnail((100, 100), Image.ANTIALIAS)
        # im.save(thumb_path, "PNG")
        file.close()
        o.icon = request.user.username+''+str(o.id)
    else:
        o.icon = ''

    for address in o.addresses.all():
        o.addresses.remove(address)

    addresses = request.POST.get('addresses').split(',')
    for address in addresses:
        if not address:
            continue
        a = Address.objects.get(pk=int(address))
        o.addresses.add(a)

    o.save()

    return HttpResponse(json.dumps({}), content_type = "application/json")

def all(request):
    if not request.user.is_authenticated():
        users = User.objects.all()
        return render_to_response('login.html', {'users': users})

    offers  = Offer.objects
    data = [o.json() for o in offers.all()]
    return HttpResponse(json.dumps(data), content_type = "application/json")

def all_mobile(request):
    uuid = request.POST.get('uuid', None)
    token = request.POST.get('push_id', None)

    try:
        user = Fuser.objects.get(uuid=uuid)
    except Fuser.DoesNotExist:
        user = None

    if user is None:
        user = Fuser()
        user.uuid = uuid
        user.token = token

    user.last_login = datetime.datetime.now()
    user.last_send = datetime.datetime.min
    user.current_lat = 0
    user.current_lng = 0

    user.save()

    offers  = Offer.objects
    data = [o.json() for o in offers.all()]
    return HttpResponse(json.dumps(data), content_type = "application/json")

def getbycompany(request):
    cid = request.POST.get('cid')

    company = Company.objects.get(pk=cid)

    data = [o.json() for o in company.offers.all()]
    return HttpResponse(json.dumps(data), content_type = "application/json")

def get(request):
    if not request.user.is_authenticated():
        users = User.objects.all()
        return render_to_response('login.html', {'users': users})

    oid = request.POST.get('oid')

    offer   = Offer.objects.get(pk=oid)

    offer.is_my = offer.company.user == request.user
    offer.all_addresses = offer.company.addresses

    return HttpResponse(json.dumps(offer.json()), content_type = "application/json")

def delete(request):
    oid = request.POST.get('oid')

    if (not oid):
        return

    o = Offer.objects.get(pk=oid)
    o.delete()

    return HttpResponse('ok')

def toFavorites(request):
    uuid = request.POST.get('uuid', None)
    oid = request.POST.get('offer_id')

    try:
        user = Fuser.objects.get(uuid=uuid)
    except Fuser.DoesNotExist:
        user = None

    if not user:
        return HttpResponse({"status": "user_not_found"}, content_type = "application/json")

    offer = Offer.objects.get(pk=oid)
    company = offer.company

    favorite= None
    try:
        favorite = UserFavorites.objects.get(user=user, company=company)
    except ObjectDoesNotExist:
        pass


    if favorite:
        favorite.delete()
        return HttpResponse({"status": "deleted"}, content_type = "application/json")

    uf = UserFavorites(user=user, company=company)
    uf.save()

    return HttpResponse({"status": "created"}, content_type = "application/json")

def category_update(request):
    uuid = request.POST['uuid']
    category_id = request.POST['category_id']
    value = request.POST['value']

    try:
        user = Fuser.objects.get(uuid=uuid)
    except Fuser.DoesNotExist:
        user = None

    if not user:
        return HttpResponse({"status": "user_not_found"}, content_type = "application/json")

    category = OfferCategory.objects.get(pk=category_id)

    user_category, created = CategoryToUser.objects.get_or_create(
         user=user,
         category=category
    )
    user_category.value = value
    user_category.save()

    return HttpResponse(json.dumps({'result': "ok"}), content_type = "application/json")