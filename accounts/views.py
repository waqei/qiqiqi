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
from forms import *
from car.models import *


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


#def requires_login(view):
#    def new_view(request, *args, **kwargs):
#        if not request.user.is_authenticated():
#            return HttpResponseRedirect('/accounts/login/')
#        return view(request,*args,**kwargs)
#    return new_view




#管理用户，传递用户
def manUser(request):
    if not request.user.is_superuser:
        return HttpResponseRedirect(reverse("404"))
    all_user=User.objects.filter(is_staff='1',is_superuser='0')
    asso_user=User.objects.filter(is_staff='0',is_active='1')
    super_user=User.objects.filter(is_superuser='1')
    template_var={
        'all_user':all_user,
        'asso_user':asso_user,
        'super_user':super_user
    }
    return render_to_response("accounts/manage_user.html",template_var,context_instance=RequestContext(request))

#审核用户
def passUser(request):
    if not request.user.is_superuser:
        return HttpResponseRedirect(reverse("404"))
    if request.GET.get('user'):
        muser=request.GET.get('user')
        user=User.objects.get(id=muser)
        user.is_staff= '1'
        user.is_staff= '1'
        user.save()
        return HttpResponse('<script>alert("已通过！");top.location="/accounts/store/manage_user"</script>')
    else:
        HttpResponseRedirect(reverse('manage_user'))
#删除用户
def deleUser(request):
    if not request.user.is_superuser:
        return HttpResponseRedirect(reverse("404"))
    if request.GET.get('user'):
            muser=request.GET.get('user')
            user=User.objects.get(id=muser)
            user.delete()
            return HttpResponse('<script>alert("已删除！");top.location="/accounts/store/manage_user"</script>')
    else:
        HttpResponseRedirect(reverse('manage_user'))


#编辑用户信息
def editUser(request):
    if not request.user.is_superuser:
        return HttpResponseRedirect(reverse("404"))
    template_var={}
    form = UserForm()
    if request.method == "POST":
        form = UserForm(request.POST.copy())
        if form.is_valid():
            username=request.user.username
            realname = form.cleaned_data['realname']
            email = form.cleaned_data['email']
            is_staff = form.cleaned_data['is_staff']
            is_superuser=form.cleaned_data['is_superuser']
            user= authenticate(username=username,first_name=realname,email=email,is_staff=is_staff,is_superuser=is_superuser)
    template_var['euser']=request.GET.get('user')
    template_var['form']=form
    return render_to_response('accounts/edit_user.html',template_var,context_instance=RequestContext(request))

#编辑商铺信息
def editStore(request):
    pass

#更改用户密码
def change_password(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse("404"))
    template = {}
    form = ChangePasswordForm()
    if request.method=="POST":
        form = ChangePasswordForm(request.POST.copy())
        if form.is_valid():
            username = request.user.username
            oldpassword = form.cleaned_data["old_password"]
            newpassword = form.cleaned_data["new_password"]
            newpassword1 = form.cleaned_data["new_password1"]
            user = authenticate(username=username,password=oldpassword)
            if user: #原口令正确
                if newpassword == newpassword1:#两次新口令一致
                    user.set_password(newpassword)
                    user.save()
                    print '1'
                    return HttpResponse('<script>alert("修改密码成功！");top.location="/accounts/changepw";</script>')
                else:#两次新口令不一致
                    template["word"] = '两次输入口令不一致'
                    template["form"] = form
                    print '2'
                    return render_to_response("accounts/change_password.html",template,context_instance=RequestContext(request))
            else:  #原口令不正确
                if newpassword == newpassword1:#两次新口令一致
                    template["word"] = '原口令不正确'
                    template["form"] = form
                    print '3'
                    return render_to_response("accounts/change_password.html",template,context_instance=RequestContext(request))
                else:#两次新口令不一致
                    template["word"] = '原口令不正确，两次输入口令不一致'
                    template["form"] = form
                    print '4'
                    return render_to_response("accounts/change_password.html",template,context_instance=RequestContext(request))
    template["form"] = form
    return render_to_response("accounts/change_password.html",template,context_instance=RequestContext(request))
