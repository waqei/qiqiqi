# _*_ coding = utf-8

from django import forms
from django.utils.translation import ugettext_lazy as _


class SearchForm(forms.Form):
    item=forms.CharField(label=(""),max_length=30)
