#coding=utf-8
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from form import ItemsForm,StoreForm,AddForm,AdForm,LinkForm
from car.models import *
import re


##############################工具函数############################
#验证是否是正整数
def IsNUM(varObj):
    rule = '^\+?[1-9][0-9]*$'
    match = re.match( rule , varObj )
    if match:
        return True
    return False


##################################################################

def addItems(request,muser):
    """
    添加商品
    """
    template_var={}
    form = ItemsForm(initial={'company':muser,})
    form['sort'].field.help_text ='按下Ctrl键支持多选'
    form['brand'].field.help_text ='按下Ctrl键支持多选'
    if request.method == 'POST':
        form = ItemsForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()

            return HttpResponse('<script>alert("添加成功！");top.location="/goods/item/manage";</script>')
    template_var['form']=form
    return  render_to_response('goods/add.html',template_var,context_instance=RequestContext(request))



#添加商铺
def addStore(request):
    template_var={}
    form=StoreForm()
    form['sell'].field.help_text ='按下Ctrl键支持多选'
    form['s_brand'].field.help_text ='按下Ctrl键支持多选'
    if request.method == 'POST':
        form = StoreForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('<script>alert("添加成功！");top.location="/goods/store/add";</script>')
        else:
            HttpResponseRedirect(reverse('add_store'))
    template_var['form']=form
    return render_to_response('goods/add_store.html',template_var,context_instance=RequestContext(request))


#添加品牌
#def addbrand(request):
#    allbrand=Brands.objects.all()
#    template_var={}
#    form=BrandForm()
#    if request.method=='POST':
#        form = BrandForm(request.POST,request.FILES)
#        if form.is_valid():
#            form.save()
#            return HttpResponse('<script>alert("添加成功");top.location="/goods/add_brand";</script>')
#        else:
#            HttpResponseRedirect(reverse('add_brand'))
#    template_var['form']=form
#    template_var['allbrand']=allbrand
#    return render_to_response('goods/add_brand.html',template_var,context_instance=RequestContext(request))
#
#
##删除品牌
#def delebrand(request,id):
#    if id:
#        dele=Brands.objects.get(id=id)
#        dele.delete()
#        return HttpResponse('<script>alert("已删除！");top.location="/goods/add_brand"</script>')
#    else:
#        HttpResponseRedirect(reverse('addbrand'))


#管理商品
def manageitems(request):
    allitem=Items.objects.all()
    allsort=Sorts.objects.all()
    allbrand=Brands.objects.all()
    template_var={
        'allitem':allitem,
        'allsort':allsort,
        'allbrand':allbrand,

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
    template_var={}
    form=AdForm()
    if request.method == 'POST':
        form=AdForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('<script>alert("添加成功");top.location="/goods/ad";</script>')
        else:
            HttpResponseRedirect(reverse('ad_manage'))
    template_var['form']=form
    return render_to_response('goods/ad.html',template_var,context_instance=RequestContext(request))


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
