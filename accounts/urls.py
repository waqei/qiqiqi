#coding=utf-8
from django.conf.urls import patterns, include, url
from accounts import views

urlpatterns = patterns('',

    url(r'^accounts/$', 'accounts.views.login',name="login"),
    url(r'^accounts/index$', 'accounts.views.index',name="admin_index"),
    url(r'^accounts/register$', 'accounts.views.register',name="register"),
    ##url(r'^accounts/login$', 'accounts.views.login',name="login"),
    url(r'^accounts/logout$', 'accounts.views.logout',name="logout"),
    url(r'^accounts/add','accounts.views.addItems',name="add_items"),

)
