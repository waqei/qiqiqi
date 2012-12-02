#coding=utf-8
from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.forms import ModelForm,Textarea
from models import Items,Stores,Sorts,Brands
from django.utils.translation import ugettext_lazy as _

class ItemsForm(ModelForm):
    class Meta:
        model=Items
        #        fields=('it_name','company','series','version','description','exit_date','price','img')
        widgets={
            'description':Textarea(attrs={'cols':10,'rows':10}),
            }


class StoreForm(ModelForm):
    class Meta:
        model=Stores
        widgets={
            'it_description':Textarea(attrs={'cols':10,'rows':10}),
            }


class SortForm(ModelForm):
    class Meta:
        model=Sorts

class BrandForm(ModelForm):
    class Meta:
        model=Brands


class AddForm(forms.Form):
    name = forms.CharField(label=_(u'名称'),max_length=10,widget=forms.TextInput(attrs={'size':10,}))

    def clean_name(self):
        '''验证重复分类'''
        name = Sorts.objects.filter(name__iexact=self.cleaned_data["name"])
        if not name:
            return self.cleaned_data["name"]
        return HttpResponse('<script>alert("该项已经存在,请检查名称");history.go(-1);</script>')
