#coding=utf-8
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from django.forms import ModelForm,Textarea
from car.models import Items,Stores,Sorts,Brands

BOOLE_CHOICES=(
    ('是','1'),
    ('否','0'),
)

class RegisterForm(forms.Form):
    email=forms.EmailField(label=_(u"邮箱"),max_length=30,widget=forms.TextInput(attrs={'size': 30,}))
    username=forms.CharField(label=_(u"用户名"),max_length=30,widget=forms.TextInput(attrs={'size': 20,}))
    password=forms.CharField(label=_(u"密码"),max_length=30,widget=forms.PasswordInput(attrs={'size': 20,}))
    re_password=forms.CharField(label=_(u"重复密码"),max_length=30,widget=forms.PasswordInput(attrs={'size': 20,}))

    def clean_username(self):
        '''验证重复昵称'''
        users = User.objects.filter(username__iexact=self.cleaned_data["username"])
        if not users:
            return self.cleaned_data["username"]
        raise forms.ValidationError(_(u"该昵称已经被使用请使用其他的昵称"))
        
    def clean_email(self):
        '''验证重复email'''
        emails = User.objects.filter(email__iexact=self.cleaned_data["email"])
        if not emails:
            return self.cleaned_data["email"]
        raise forms.ValidationError(_(u"该邮箱已经被使用请使用其他的"))
        
class LoginForm(forms.Form):
    username=forms.CharField(label=_(u"用户名"),max_length=30,widget=forms.TextInput(attrs={'size': 20,}))
    password=forms.CharField(label=_(u"密码"),max_length=30,widget=forms.PasswordInput(attrs={'size': 20,}))





class UserForm(forms.Form):
    realname=forms.CharField(label=_(u"真实姓名"),max_length=10,widget=forms.TextInput(attrs={'size':10,}))
    email=forms.EmailField(label=_(u"E-mail"),max_length=30,widget=forms.TextInput(attrs={'size':30,}))
    is_staff=forms.ChoiceField(label=_(u"是否商户",widget=forms.Select(choices=BOOLE_CHOICES)))
    is_superuser=forms.ChoiceField(label=_(u"是否管理员",widget=forms.Select(choices=BOOLE_CHOICES)))

    def clean_email(self):
        emails = User.objects.filter(email__iexact=self.cleaned_data["email"])
        if not emails:
            return self.cleaned_data["email"]
        raise forms.ValidationError(_(u"该邮箱已经被使用请使用其他的"))


class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(label=_(u"原密码"),max_length=30,widget=forms.PasswordInput(attrs={'size': 20,}))
    new_password = forms.CharField(label=_(u"新密码"),max_length=30,widget=forms.PasswordInput(attrs={'size': 20,}))
    new_password1 = forms.CharField(label=_(u"新密码确认"),max_length=30,widget=forms.PasswordInput(attrs={'size': 20,}))
