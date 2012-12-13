#coding=utf-8

from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.admin import User
from form import *

#from django.template.loader import get_template
#from django.template import Template,Context
from car.models import *

def index(request):
    template_var={}
    #links
    links=Links.objects.all()
    #sorts
    parents=Sorts.objects.filter(level= 0)
    #ad_5
    ad_6=Ad_6.objects.latest('id')
    #ad_middle
    ad_middle=Ad_middle.objects.latest('id')

    template_var={
        'links':links,
        'parents':parents,
        'ad_6':ad_6,
        'ad_middle':ad_middle,
    }

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
#
#def classify(request,sort):
#    template_var={}
#    if sort:
#        items = Items.objects.filter(sort__icontains=sort)
#        if items =="":
#            HttpResponse("<script>alert('不存在该分类!');history .go(-1);</script>")
#    else:
#        items=Items.objects.all()
#
#    template_var['items'] = items
#    return render_to_response('index/classify.html',template_var,context_instance=RequestContext(request))

def classify(request):
    return render_to_response('index/classify.html')

def test(request):
    return render_to_response('accounts/test.html')


#store

def store(request,id):
    store=Stores.objects.get(boss=id)
    boss=User.objects.get(id=id)
    form=SearchForm()
    if request.method == 'POST':
        form=SearchForm(request.POST)
        if form.is_valid():
            p=form.cleaned_data['item']
            result=Items.objects.filter(company=id,it_name__contains=p)
            if result:
                return result
            else:
                result['1']='您查找的产品不存在'

    template_var={
        'boss':boss,
        'com':store,
    }
    return render_to_response('store/base-store.html',template_var)
