#coding=utf-8
from django.conf.urls import patterns, include, url
from car.models import Stores,Items

urlpatterns = patterns('',

    #index
#    url(r'^$', 'index.view.index',name='index'),

    #classify
    url(r'classify/(?P<id>\b.*).html/(?P<p>\b.*)$','index.view.classify',name='classify'),
#    url(r'classify/$','index.view.classify',name='classify'),



    url(r'search/its/(?P<name>\w.*)$','index.view.search',{'model':Items}),
    url(r'search/stores/(?P<name>\W.*)$','index.view.search',{'model':Stores}),
    url(r'test','index.view.test',name='test'),
)
