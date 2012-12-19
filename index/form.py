# _*_ coding = utf-8

from django import forms
from django.forms import ModelForm,Textarea,HiddenInput
from django.utils.translation import ugettext_lazy as _
from car.models import Messages


class SearchForm(forms.Form):
    item=forms.CharField(label=(""),max_length=30)

class MessageForm(ModelForm):
    class Meta:
        fields=('contact_number','content')
        model = Messages
        widgits={
            'store':HiddenInput,
            'is_read':HiddenInput(attrs={'value':'0'}),
            'content':Textarea(attrs={'cols':20,'rows':20})
        }