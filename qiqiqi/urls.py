#coding=utf-8
from django.conf.urls import patterns, include, url
from car import views
from index import view
from django.contrib import admin
admin.autodiscover()
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'qiqiqi.views.home', name='home'),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    #index
    url(r'^$', 'index.view.index',name='index'),
    url(r'search/$',view.search),

    #account pages

    url(r'^accounts/$', 'accounts.views.login',name="login"),
    url(r'^accounts/index$', 'accounts.views.index',name="admin_index"),
    url(r'^accounts/register$', 'accounts.views.register',name="register"),
    url(r'^accounts/logout$', 'accounts.views.logout',name="logout"),


    ##item

    url(r'^accounts/item/add','accounts.views.addItems',name="add_items"),

    ##store

    url(r'^accounts/store/add','accounts.views.addStore',name="add_store"),
    url(r'^accounts/store/manage_user','accounts.views.manUser',name="manage_user"),
    url(r'^accounts/store/delete/$','accounts.views.deleUser',name="delete_user"),
    url(r'^accounts/store/pass/$','accounts.views.passUser',name="pass_user"),
    url(r'^accounts/store/edit/$','accounts.views.editUser',name="pass_user"),
    url(r'^accounts/store/edit_store$','accounts.views.editStore',name="edit_store"),

    #static items

    url(r'^static/(?P<path>.*)$','django.views.static.serve',{'static_root':settings.STATIC_ROOT}),

    #errors

    url(r'^404$','index.view.err_404',name="404"),
)
