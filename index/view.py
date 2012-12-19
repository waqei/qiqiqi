#coding=utf-8

from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.admin import User
from form import SearchForm,MessageForm
from car.models import Links,Items,Sorts,Ad_6,Ad_middle,Stores,Messages
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
    try:
        st_nu=Stores.objects.all().count()
        if st_nu >= 5:
            new_stores=Stores.objects.extra(
                select={
                    'id':'select top 5 * order by id desc'
                }
            )
        else:
            new_stores = Stores.objects.all()
    except ValueError:
            new_stores=Stores.objects.all()

    #new_items
    try:
        it_nu=Items.objects.all().count()
        if it_nu >= 5:
            new_items=Items.objects.extra(
                select={
                    'id':'select top 5 * order by id desc'
                }
            )
        else:
            new_items=Items.objects.all()
    except ValueError:
        new_items=Items.objects.all()

        #new_items
    try:
        mess_nu=Messages.objects.all().count()
        if mess_nu >= 5:
            messages=Messages.objects.extra(
                select={
                    'id':'select top 5 * order by id desc'
                }
            )
        else:
            messages=Messages.objects.all()
    except ValueError:
        messages=Messages.objects.all()

    template_var={
        'DOMAIN':DOMAIN,
        'messages':messages,
        'new_items':new_items,
        'new_stores':new_stores,
        'links':links,
        'parents':parents,
        'ad_6':ad_6,
        'ad_middle':ad_middle,
    }
    return render_to_response("index/index.html",template_var,context_instance=RequestContext(request))

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
def store(request,store_id):
    store=Stores.objects.get(boss=store_id)
    boss=User.objects.get(id=store_id)
    items=Items.objects.filter(company=store)
    form=SearchForm()
    if request.method == 'POST':
        form=SearchForm(request.POST)
        if form.is_valid():
            p=form.cleaned_data['item']
            result=Items.objects.filter(company=store_id,it_name__contains=p)
            if result:
                return result
            else:
                result.error='您查找的产品不存在'
    template_var={
        'items':items,
        'boss':boss,
        'com':store,
        'form':form,
    }
    return render_to_response('store/index.html',template_var,context_instance=RequestContext(request))

##store information
def storeInfo(request,store_id):
    store=Stores.objects.get(boss=store_id)
    boss=User.objects.get(id=store_id)
    template_var={
        'boss':boss,
        'com':store,
    }
    return render_to_response('store/info.html',template_var,context_instance=RequestContext(request))



def classify_s(request,store_id,sort_id,p):
    page_size=10
    after_range_num = 5
    before_range_num = 6

    store=Stores.objects.get(boss=store_id)
    if sort_id == "0":
        sorts=Sorts.objects.filter(level = 0)
        items=Items.objects.all().filter(company=store_id)
        if items is None:
            HttpResponse("<script>alert('尚无产品!');history.go(-1);</script>")
    elif sort_id:
        sorts=Sorts.objects.filter(parent=sort_id)
        sort=Sorts.objects.get(id=sort_id)
        items = sort.items_set.all().filter(company=store_id)

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
        'store':store,
        'sorts':sorts,
        'items':items,
        'page_range':page_range,
        }
    return render_to_response('store/classify.html',template_var,context_instance=RequestContext(request))


def views(request,store_id,item_id):
    store=Stores.objects.get(boss=store_id)
    item=Items.objects.get(id=item_id)

    template_var={
        'com':store,
        'item':item,
    }
    return render_to_response('store/view.html',template_var,context_instance=RequestContext(request))

def comment_done(request):
    return HttpResponse('<script>alert("提交成功");location.href=document.referrer;;</script>')

def message(request,store_id):
    store=Stores.objects.get(boss=store_id)
    messages=Messages.objects.all()
    form=MessageForm()
    if request.method == 'POST':
        form=MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('<script>alert("提交成功");top.location="/goods/ad";</script>')
        else:
            return HttpResponse('<script>alert("提交失败");location.href=document.referrer;</script>')
    template_var={
        'messages':messages,
        'com':store,
        'form':form,
    }
    return render_to_response('store/message.html',template_var,context_instance=RequestContext(request))

def ok(request):
    return render_to_response('store/ok.html',context_instance=RequestContext(request))