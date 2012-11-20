#coding=utf-8
import time
from qiqiqi import settings
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login ,logout as auth_logout
from django.utils.translation import ugettext_lazy as _
from forms import RegisterForm,LoginForm,ItemsForm,StoreForm

import ImageFile
from car.models import Items,Stores
import os

def index(request):
    '''首页视图'''
    template_var={"w":_(u"欢迎您 游客!")}
    if request.user.is_authenticated():
        template_var["w"]=_(u"欢迎您 %s!")%request.user.username
    return render_to_response("accounts/welcome.html",template_var,context_instance=RequestContext(request))

def register(request):
    '''注册视图'''
    template_var={}
    form = RegisterForm()
    if request.method=="POST":
        form=RegisterForm(request.POST.copy())
        if form.is_valid():
            username=form.cleaned_data["username"]
            email=form.cleaned_data["email"]
            password=form.cleaned_data["password"]
            user=User.objects.create_user(username,email,password)
            user.save()
            _login(request,username,password)#注册完毕 直接登陆
            return HttpResponseRedirect(reverse("index"))
    template_var["form"]=form
    return render_to_response("accounts/register.html",template_var,context_instance=RequestContext(request))

def login(request):
    '''登陆视图'''
    template_var={}
    form = LoginForm()
    if request.method == 'POST':
        form=LoginForm(request.POST.copy())
        if form.is_valid():
            _login(request,form.cleaned_data["username"],form.cleaned_data["password"])
            return HttpResponseRedirect(reverse("admin_index"))
    template_var["form"]=form
    return render_to_response("accounts/login.html",template_var,context_instance=RequestContext(request))

def _login(request,username,password):
    '''登陆核心方法'''
    ret=False
    user=authenticate(username=username,password=password)
    if user:
        if user.is_active:
            auth_login(request,user)
            ret=True
        else:
            messages.add_message(request, messages.INFO, _(u'用户没有激活'))
    else:
        messages.add_message(request, messages.INFO, _(u'用户不存在'))
    return ret

def logout(request):
    '''注销视图'''
    auth_logout(request)
    return HttpResponseRedirect(reverse('index'))


def addItems(request):
    """
    添加商品
    """
    template_var={}
    form = ItemsForm()
    if request.method == 'POST':
        form = ItemsForm(request.POST.copy())
        if form.is_valid():
            name=form.cleaned_data['name']
            store=form.cleaned_data['store']
            series=form.cleaned_data['series']
            version=form.cleaned_data['version']
            description=form.cleaned_data['description']
            exit_date=form.cleaned_data['exit_date']
            price=form.cleaned_data['price']
            item=Items(it_name=name,
                company=store,
                series=series,
                version=version,
                description=description,
                exit_date=exit_date,
                price=price
            )
            item.save()
            _upload('imagefiles')
    template_var['form']=form
    return  render_to_response('accounts/add.html',template_var,context_instance=RequestContext(request))

def _upload(file):
    '''图片上传函数'''
    if file:
        path=os.path.join(settings.MEDIA_ROOT,'upload')
        file_name=str(time.strftime("%y%m%d%H%M%S",time.localtime()))+".jpg"
        path_file=os.path.join(path,file_name)
        parser = ImageFile.Parser()
        for chunk in file.chunks():
            parser.feed(chunk)
        img = parser.close()
        try:
            if img.mode != "RGB":
                img = img.convert("RGB")
            img.save(path_file, 'jpeg',quality=100)
        except:
            return False
        return True
    return False

def addStore(request):
    template_var={}
    form=StoreForm()
    if request.method == 'POST':
        form = StoreForm(request.POST.copy())
        if form.is_valid():
            st_name=form.cleaned_data['st_name']
            boss=form.cleaned_data['boss']
            address=form.cleaned_data['address']
            tele=form.cleaned_data['tele']
            it_description=form.cleaned_data['it_description']
            email=form.cleaned_data['email']

            store=Stores(
                st_name=st_name,
                boss=boss,
                address=address,
                tele=tele,
                it_description=it_description,
                email=email,
            )
    template_var['form']=form
    return render_to_response('accounts/add_store.html',template_var,context_instance=RequestContext(request))