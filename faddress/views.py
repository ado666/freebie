from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.conf import settings
from faddress.models import Address
from fcompany.models import Company
import datetime
import json


# Create your views here.
def save(request):
    aid     = request.POST.get('id')
    cid     = request.POST.get('cid')
    name    = request.POST.get('name')

    lat      = request.POST.get('lat')
    lng      = request.POST.get('lng')

    if aid:
        a = Address.objects.get(pk=aid)
    else:
        a = Address()
    print(lat, lng, cid, aid)
    company = Company.objects.get(pk=cid)

    a.company  = company
    a.name  = name

    a.lat   = lat
    a.lng   = lng

    a.save()

    return HttpResponse(json.dumps({}), content_type = "application/json")

def getbycompany(request):
    cid = request.POST.get('cid')

    company = Company.objects.get(pk=cid)

    data = [a.json() for a in company.addresses.all()]
    return HttpResponse(json.dumps(data), content_type = "application/json")

def all(request):
    data = [a.json() for a in Address.objects.all()]
    return HttpResponse(json.dumps(data), content_type = "application/json")

def get(request):
    if not request.user.is_authenticated():
        users = User.objects.all()
        return render_to_response('login.html', {'users': users})

    aid = request.POST.get('aid')

    address = Address.objects.get(pk=aid)

    address.is_my = address.company.user == request.user

    return HttpResponse(json.dumps(address.json()), content_type = "application/json")

def delete(request):
    aid = request.POST.get('oid')

    if (not aid):
        return

    a = Address.objects.get(pk=aid)
    a.delete()

    return HttpResponse('ok')

