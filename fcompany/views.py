from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.conf import settings
from fcompany.models import Company
# Create your views here.

def save(request):
    if not request.user.is_authenticated():
        users = User.objects.all()
        return render_to_response('login.html', {'users': users})

    name = request.POST.get('name')
    desc = request.POST.get('desc')
    cid  = request.POST.get('cid')

    if cid:
        c = Company.objects.get(pk=cid)
    else:
        c = Company()

    c.name = name
    c.desc = desc
    c.user = request.user

    if request.FILES:
        file = request.FILES['file']
        path = settings.IMAGES_DIR + '/' + request.user.username + cid + '.png'
        fout = open(path,'w')
        fout.write(file.read())
        file.close()
        c.icon = request.user.username+''+cid

    c.save()

    return HttpResponse('/')