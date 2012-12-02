#coding=utf-8
from django.forms import ModelForm,Textarea
from models import Items,Stores,Sorts,Brands


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

