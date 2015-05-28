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
    file = None
    if request.FILES:
        file = request.FILES['file']

    path = settings.IMAGES_DIR + '/' + request.user.username + '/' + name + '.png'

    if cid:
        c = Company.objects.get(pk=cid)
    else:
        c = Company()

    if c.icon != file:
        need_save_image = True

    c.name = name
    c.desc = desc
    if file:
        c.icon = request.user.username + '/' + name + '.png'
    else:
        c.icon = '/' + 'default' + '.png'
    c.save()

    if need_save_image:
        fout = open(path,'w')
        fout.write(file.read())
        file.close()

    return HttpResponse('/')