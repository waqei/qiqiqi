#coding=utf-8
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from form import ItemsForm,StoreAdForm,StoreForm,EditStoreForm,LinkForm,AddForm,ItemsStaffForm,NewsForm
from car.models import *
import re
from qiqiqi.settings import DOMAIN

##############################工具函数############################
#验证是否是正整数
def IsNUM(varObj):
    rule = '^\+?[1-9][0-9]*$'
    match = re.match( rule , varObj )
    if match:
        return True
    return False


##################################################################
#添加商品
def addItems(request):
    if request.user.is_superuser:
        form = ItemsForm()
        form['sort'].field.help_text ='<p class="alert alert-info">按下Ctrl键支持多选</p>'
        form['exit_date'].field.help_text ='<p class="alert alert-info">日期格式&nbsp;<strong><em>2012-12-21</em></strong></p>'
        if request.method == 'POST':
            form = ItemsForm(request.POST,request.FILES)
            if form.is_valid():
                form.save()
            return HttpResponse('<script>alert("添加成功！");top.location="/goods/item/manage";</script>')
    elif request.user.is_staff:
        muser=request.user
        form = ItemsStaffForm()
        form['sort'].field.help_text ='<p class="alert alert-info">按下Ctrl键支持多选</p>'
        form['exit_date'].field.help_text ='<p class="alert alert-info">日期格式<strong><em>2012-12-21</em></strong></p>'
        if request.method =='POST':
            form = ItemsStaffForm(request.POST,request.FILES)
#            form.initial={'company':muser.stores}
            if form.is_valid():
                form.save()
#            it_name=form.cleaned_data['it_name']
#            company = muser.stores
#            sort=form.cleaned_data['sort']
#            brand=form.cleaned_data['brand']
#            version=form.cleaned_data['version']
#            description=form.cleaned_data['description']
#            exit_date=form.cleaned_data['exit_date']
#            price=form.cleaned_data['price']
#            img =form.cleaned_data['img']
#            item=Items
#            item.it_name=it_name
#            item.company=company
#            item.sort=sort
#            item.brand=brand
#            item.version=version
#            item.description=description
#            item.exit_date=exit_date
#            item.price=price
#            item.img=img
#            item.save()
                return HttpResponse('<script>alert("添加成功！");top.location="/goods/item/manage";</script>')

    else:
        return HttpResponseRedirect(reverse("404"))

    template_var={
        'form':form,
    }
    return  render_to_response('goods/add.html',template_var,context_instance=RequestContext(request))


#添加商铺
def addStore(request):
    if not request.user.is_superuser:
        return HttpResponseRedirect(reverse("404"))
    template_var={}
    form=StoreForm()
    if request.method == 'POST':
        form = StoreForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('<script>alert("添加成功！");top.location="/goods/store/add";</script>')
        else:
            HttpResponseRedirect(reverse('add_store'))
    template_var['form']=form
    return render_to_response('goods/add_store.html',template_var,context_instance=RequestContext(request))
#show store info
def showStoreinfo(request):
    id=request.user.id
    store=Stores.objects.get(boss=id)
    template_var={}
    template_var['com']=store
    return render_to_response('goods/storeinfo.html',template_var,context_instance=RequestContext(request))

#edit store info
def editStore(request):
    id=request.user.id
    store=Stores.objects.get(boss=id)
    form=EditStoreForm()
    template_var={}
    if request.method == 'POST':
        form = EditStoreForm(request.POST,request.FILES)
        if form.is_valid():
            url = DOMAIN+"/store/" + str(store.id) + "/"
            name=form.cleaned_data['name']
            tel=form.cleaned_data['tel']
            qq=form.cleaned_data['qq']
            address=form.cleaned_data['address']
#            sell=form.cleaned_data['sell']
            notice=form.cleaned_data['notice']
            it_description=form.cleaned_data['it_description']
            Stores.objects.filter(boss=id).update(url=url,name=name,tel=tel,qq=qq,address=address,
                        notice=notice,it_description=it_description)
            return HttpResponse('<script>alert("添加成功！");top.location="/goods/store/edit/";</script>')
        else:
            return HttpResponse('<script>alert("修改失败！");top.location="/goods/store/edit/";</script>')
    template_var['form']=form
    return render_to_response('goods/editstore.html',template_var,context_instance=RequestContext(request))

#add store ad
def storeAd(request):
    id=request.user.id
    store=Stores.objects.get(boss=id)
    form=StoreAdForm()
    template_var={}
    if request.method == 'POST':
        form = StoreAdForm(request.POST,request.FILES)
        if form.is_valid():
            logo=form.cleaned_data['logo']
            loc1=form.cleaned_data['loc1']
            loc2=form.cleaned_data['loc2']
            loc3=form.cleaned_data['loc3']
            store.logo=logo
            store.loc1=loc1
            store.loc2=loc2
            store.loc3=loc3
            store.save()
            return HttpResponse('<script>alert("修改成功！");history.go(-1);</script>')
    template_var['form']=form
    return render_to_response('goods/editstoread.html',template_var,context_instance=RequestContext(request))

#管理商品
def manageitems(request):
    allsort=Sorts.objects.all()
    if request.user.is_superuser:
        allitem=Items.objects.all()
    elif request.user.is_staff:
        allitem=Items.objects.filter(company=request.user.stores)

    else:
        return HttpResponseRedirect(reverse("404"))

    template_var={
        'allitem':allitem,
        'allsort':allsort,

        }
    return render_to_response("goods/manage_item.html",template_var,context_instance=RequestContext(request))



#显示分类
def show_sort(request):
    return render_to_response("goods/show_sort.html",
        {'nodes':Sorts.objects.all()},
        context_instance=RequestContext(request))

#添加子分类
def add_sort(request,parent):
    template_var={}
    form = AddForm()

    if request.method=="POST":
        form = AddForm(request.POST.copy())
        if form.is_valid():
            if parent!="root" and parent:
                sortname=form.cleaned_data['name']
                par=Sorts.objects.get(name=parent)
                Sorts.objects.create(name=sortname,parent=par,)
                return HttpResponse('<script>alert("添加成功");top.location="/goods/show_sort/";</script>')
            elif parent == "root":
                sortname=form.cleaned_data['name']
                Sorts.objects.create(name=sortname)
                return HttpResponse('<script>alert("添加成功");top.location="/goods/show_sort/";</script>')
            else:
                return HttpResponse('<script>alert("填写错误!");history.go(-1);</script>')
    template_var['par']=parent
    template_var['form']=form
    return  render_to_response("goods/add_sort.html",template_var,context_instance=RequestContext(request))


#删除
def dele(request,id,model):
    if IsNUM(id):
        p=model.objects.filter(id=id)
        if p:
            p.delete()
        else:
            return HttpResponse('<script>alert("删除对象不存在");top.location="/accounts/index";</script>')
        return HttpResponse('<script>alert("删除成功");location.href=document.referrer;</script>')
    else:
        return HttpResponse('<script>alert("删除错误!");top.location="/accounts/index";</script>')



#广告管理
def ad(request):
    return render_to_response('goods/ad/ad.html',context_instance=RequestContext(request))


def ad_m(request,Form):
    template_var={}
    form=Form()
    if request.method == 'POST':
        form=Form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('<script>alert("添加成功");top.location="/goods/ad";</script>')
        else:
            HttpResponseRedirect(reverse('ad_manage'))
    template_var['form']=form
    return render_to_response('goods/ad/ad_6.html',template_var,context_instance=RequestContext(request))



#友情链接管理
def links(request):
    template_var={}
    alllinks=Links.objects.all()
    form=LinkForm()
    form['url'].field.help_text ='<p class="alert alert-info">请输入有效网址,包含&nbsp;<em><strong>http://</strong></em></p>'
    if request.method == 'POST':
        form = LinkForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('<script>alert("添加成功");top.location="/goods/links";</script>')
        else:
            HttpResponseRedirect(reverse('m_links'))
    template_var['alllinks']=alllinks
    template_var['form']=form
    return  render_to_response('goods/link.html',template_var,context_instance=RequestContext(request))

#news
def news(request):
    if request.user.is_superuser:
        allnews=News.objects.all()
        form=NewsForm()
        if request.method == "POST":
            form=NewsForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponse('<script>alert("添加成功");top.location="/goods/news";</script>')
            else:
                HttpResponseRedirect(reverse('news'))
        template_var={
            'allnews':allnews,
            'form':form,
        }
        return render_to_response('goods/news/news.html',template_var,context_instance=RequestContext(request))

