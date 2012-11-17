#coding=utf-8
from django.conf.urls import patterns, include, url
from car import views
from index import view


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'qiqiqi.views.home', name='home'),
    # url(r'^qiqiqi/', include('qiqiqi.foo.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
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
    ##url(r'^accounts/login$', 'accounts.views.login',name="login"),
    url(r'^accounts/logout$', 'accounts.views.logout',name="logout"),
    url(r'^accounts/add','accounts.views.addItems',name="add_items"),

    #static items
    url(r'^static/(?P<path>.*)$','django.views.static.serve',{'static_root':settings.STATIC_ROOT}),

    #errors
    url(r'^404$','index.view.err_404',name="404"),
)
