#coding=utf-8

from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.admin import User
from form import SearchForm

from car.models import Links,Items,Sorts,Ad_6,Ad_middle,Stores
from qiqiqi.settings import DOMAIN
#分页模块Pagination
from django.core.paginator import Paginator,InvalidPage,EmptyPage,PageNotAnInteger


#index page
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
    #new_stores
    new_stores=Stores.objects.extra('')

    template_var={
        'DOMAIN':DOMAIN,
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

def classify(request,id,p):
    page_size=10
    after_range_num = 5
    before_range_num = 6


    if id == "0":
        sorts=Sorts.objects.filter(level = 0)
        items=Items.objects.all()

        if items is None:
            HttpResponse("<script>alert('尚无产品!');history.go(-1);</script>")
    elif id:
        sorts=Sorts.objects.filter(parent=id)
        sort=Sorts.objects.get(id=id)
        items = sort.items_set.all()

        if items == '':
            HttpResponse("<script>alert('不存在该分类!');history.go(-1);</script>")
    else:
        HttpResponse("<script>alert('查询错误!');history.go(-1);</script>")

    try:
        page = int(p)
        if page < 1:
            page = 1
    except ValueError:
        page = 1
    paginator = Paginator(items,page_size)
    try:
        items = paginator.page(page)
    except(EmptyPage,InvalidPage,PageNotAnInteger):
        items = paginator.page(1)
    if page >= after_range_num:
        page_range = paginator.page_range[page-after_range_num:page+before_range_num]
    else:
        page_range = paginator.page_range[0:int(page)+before_range_num]

    template_var={
        'sorts':sorts,
        'items':items,
        'page_range':page_range,
    }
    return render_to_response('index/classify.html',template_var,context_instance=RequestContext(request))

def test(request):
    return render_to_response('accounts/test.html')


#store index
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
                result.error='您查找的产品不存在'
    template_var={
        'boss':boss,
        'com':store,
        'form':form,
    }
    return render_to_response('store/index.html',template_var,context_instance=RequestContext(request))

##store information
def storeInfo(request,id):
    store=Stores.objects.get(boss=id)
    boss=User.objects.get(id=id)
    template_var={
        'boss':boss,
        'com':store,
    }
    return render_to_response('store/info.html',template_var,context_instance=RequestContext(request))