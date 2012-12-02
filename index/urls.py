#coding=utf-8
from django.conf.urls import patterns, include, url
from index import view

urlpatterns = patterns('',

    #index
    url(r'^$', 'index.view.index',name='index'),
    url(r'search/$',view.search),
    url(r'test','index.view.test',name='test'),

)
