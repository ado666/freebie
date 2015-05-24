from django.shortcuts import render
from django.shortcuts import render_to_response
# Create your views here.

def select_template(request):
    return render_to_response('new_company.html')