from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.conf import settings
from foffer.models import Offer
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

    lat      = request.POST.get('lat')
    lng      = request.POST.get('lng')

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

    # o.lat   = lat
    # o.lng   = lng

    if url == 'img/blank.png':
        o.icon = ''

    o.save()

    if request.FILES:
        file = request.FILES['file']
        path = settings.IMAGES_DIR + '/offers/' + request.user.username + str(o.id) + '.png'
        thumb_path = settings.IMAGES_DIR + '/pins/' + request.user.username + str(o.id) + '.png'
        fout = open(path,'w')
        fout.write(file.read())
        im = Image.open(file)
        im.thumbnail((100, 100), Image.ANTIALIAS)
        im.save(thumb_path, "PNG")
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

