#coding=utf-8
from django.conf.urls import patterns, include, url



urlpatterns = patterns('',

    url(r'^$', 'accounts.views.login',name="login"),
    url(r'^index$', 'accounts.views.index',name="admin_index"),
    url(r'^register$', 'accounts.views.register',name="register"),
    url(r'^logout$', 'accounts.views.logout',name="logout"),
    url(r'^changepw$', 'accounts.views.change_password',name="changepw"),


    url(r'^store/manage_user','accounts.views.manUser',name="manage_user"),
    url(r'^store/delete/$','accounts.views.deleUser',name="delete_user"),
    url(r'^store/pass/$','accounts.views.passUser',name="pass_user"),
    url(r'^store/edit_user/(?P<userid>\w.*).html$','accounts.views.editUser',name="edit_user"),
    url(r'^store/edit_store$','accounts.views.editStore',name="edit_store"),

)