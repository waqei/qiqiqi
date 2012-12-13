#coding=utf-8
from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.forms import ModelForm,Textarea
from models import Items,Stores,Sorts,Ad_6,Links,Ad_middle
from django.utils.translation import ugettext_lazy as _

class ItemsForm(ModelForm):
    class Meta:
        model=Items
        #        fields=('it_name','company','series','version','description','exit_date','price','img')
        widgets={
            'description':Textarea(attrs={'cols':10,'rows':10}),
            }
#add store
class StoreForm(ModelForm):
    class Meta:
        model=Stores
        fields=('boss','name',)


#edit store
class EditStoreForm(ModelForm):
    class Meta:
        fields=('name','tel','qq','address','notice','it_description')
        model=Stores
        widgets={
            'notice':Textarea(attrs={'cols':10,'rows':10}),
            'it_description':Textarea(attrs={'cols':10,'rows':10}),
            }
#store ad
class StoreAdForm(forms.Form):
    logo=forms.ImageField(label=_(u'Logo'))
    loc1=forms.ImageField(label=_(u'广告1'))
    loc2=forms.ImageField(label=_(u'广告2'))
    loc3=forms.ImageField(label=_(u'广告3'))


#sort form
class SortForm(ModelForm):
    class Meta:
        model=Sorts


class AddForm(forms.Form):
    name = forms.CharField(label=_(u'名称'),max_length=10,widget=forms.TextInput(attrs={'size':10,}))

    def clean_name(self):
        '''验证重复分类'''
        name = Sorts.objects.filter(name__iexact=self.cleaned_data["name"])
        if not name:
            return self.cleaned_data["name"]
        raise forms.ValidationError(_(u"该项已经被使用请使用其他的"))



class Ad6Form(ModelForm):
    class Meta:
        model=Ad_6

class AdmiddleForm(ModelForm):
    class Meta:
        model=Ad_middle

class LinkForm(ModelForm):
    class Meta:
        model=Links