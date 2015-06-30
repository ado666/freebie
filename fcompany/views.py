from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.conf import settings
from fcompany.models import Company
import json
# Create your views here.

def save(request):
    if not request.user.is_authenticated():
        users = User.objects.all()
        return render_to_response('login.html', {'users': users})

    name = request.POST.get('name')
    desc = request.POST.get('desc')
    cid  = request.POST.get('cid')
    url  = request.POST.get('img_url')

    if cid:
        c = Company.objects.get(pk=cid)
    else:
        c = Company()
        c.user = request.user

    if url == 'img/blank.png':
        c.icon = ''

    c.name = name
    c.desc = desc

    c.save()
    if request.FILES:
        file = request.FILES['file']
        path = settings.IMAGES_DIR + '/companies/' + request.user.username + str(c.id) + '.png'
        fout = open(path,'w')
        fout.write(file.read())
        file.close()
        c.icon = request.user.username+''+str(c.id)

    c.save()

    return HttpResponse('/')

def get(request):
    if not request.user.is_authenticated():
        users = User.objects.all()
        return render_to_response('login.html', {'users': users})

    id  = request.POST.get('id')
    c   = Company.objects.get(pk=id)

    c.is_my = c.user == request.user

    return HttpResponse(json.dumps(c.json()), content_type = "application/json")


def getall(request):
    if not request.user.is_authenticated():
        users = User.objects.all()
        return render_to_response('login.html', {'users': users})

    data = [c.json() for c in Company.objects.all()]
    return HttpResponse(json.dumps(data), content_type = "application/json")

def delete(request):
    cid = request.POST.get('cid')

    if (not cid):
        return

    c = Company.objects.get(pk=cid)
    c.delete()

    return HttpResponse('/')