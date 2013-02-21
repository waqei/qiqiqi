#coding=utf-8
from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.forms import ModelForm,Textarea,HiddenInput
from models import Items,Stores,Sorts,Ad_6,Links,Ad_middle,News
from django.utils.translation import ugettext_lazy as _

class ItemsForm(ModelForm):
    class Meta:
        model=Items
        #        fields=('it_name','company','series','version','description','exit_date','price','img')
        widgets={
            'description':Textarea(attrs={'cols':10,'rows':10}),
            }

class ItemsStaffForm(ModelForm):
    class Meta:
        model=Items
        fields=('it_name','company','sort','brand','version','description','exit_date','price','img')
        widgets={
#            'company':HiddenInput,
            'description':Textarea(attrs={'cols':10,'rows':10}),
            }
#class ItemsStaffForm(forms.Form):
#    it_name=forms.CharField(max_length=10,verbose_name='商品名称')
#    sort=forms.ChoiceField()
#    brand=forms.CharField(max_length=10,verbose_name='品牌',blank=True)
#    version=forms.CharField(max_length=60,verbose_name='其他参数',blank=True)
#    description=forms.CharField(max_length=200,verbose_name='描述')
#    exit_date=forms.DateField(verbose_name='上市时间',blank=True)
#    price=forms.CharField(max_length=20,verbose_name='价格')
#    img=forms.ImageField(verbose_name='商品图片',upload_to='image',blank=True)

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

#news
class NewsForm(ModelForm):
    class Meta:
        felids=('title','content')
        model = News
        widgets={
            'content':Textarea(attrs={'cols':10,'rows':10})
        }
