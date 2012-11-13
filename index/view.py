#coding=utf-8

from django.shortcuts import render_to_response
from django.http import HttpResponse
#from django.template.loader import get_template
#from django.template import Template,Context
from car.models import Items

def index(request):
    return render_to_response('index.html')

def search(request):
    error=False
    if 'q' in request.GET and request.GET['q']:
        q=request.GET['q']

        if not q:
            error=True
        else:
            cars=Items.objects.filter(it_name__icontains=q)
            return render_to_response('index.html',
                {'cars':cars,'qurry':q}
            )
    else:
        return render_to_response('index.html',{'error':error})
