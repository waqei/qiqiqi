#coding=utf-8

from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext
#from django.template.loader import get_template
#from django.template import Template,Context
from car.models import *

def index(request):
    template_var={}
    #links
    links=Links.objects.all()
    template_var['links']=links

    #sorts
    parents=Sorts.objects.filter(level= 0)
    template_var['parents']=parents

    #ad_5
    ad_5=Ads.objects.latest('id')
    template_var['ad_5']=ad_5

    return render_to_response("index/index2.html",template_var,context_instance=RequestContext(request))

def err_404(request):
    return  render_to_response('404.html')

#商品搜索功能
def search(request,model,name):
    template_var={}
    if name:
        result=model.object.filter(itname__icontains=name)
        template_var['result']=result
    else:
        return HttpResponse("<script>alert('输入错误!');history.go(-1);</script>")
    return render_to_response("index/result.html",template_var,context_instance=RequestContext(request))



#ad manager
def ad(request):
    pass


def test(request):
    return render_to_response('accounts/test.html')

