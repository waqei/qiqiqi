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
            re_password=form.cleaned_data["re_password"]
            if password==re_password:
                user=User.objects.create_user(username,email,password)
                user.save()
                _login(request,username,password)#注册完毕 直接登陆
                return HttpResponse('<script>alert("提交成功，等待管理员认证！");top.location="/accounts/"</script>')
            else:
                return HttpResponse('<script>alert("两次密码必须相同！");history.go(-1);</script>')
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
        form = ItemsForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('<script>alert("添加成功！");history.go(0);</script>')
    template_var['form']=form
    return  render_to_response('accounts/add.html',template_var,context_instance=RequestContext(request))

def addStore(request):
    template_var={}
    form=StoreForm()
    if request.method == 'POST':
        form = StoreForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            return HttpResponse('<script>alert("添加成功！");history.go(0);</script>')
    template_var['form']=form
    return render_to_response('accounts/add_store.html',template_var,context_instance=RequestContext(request))

def manUser(request):
    template_var={}
    user=User.objects.filter(is_staff='0')
    template_var['user']=user
    return render_to_response("accounts/manage_user.html",template_var,context_instance=RequestContext(request))