#coding=utf-8
from django.conf.urls import patterns, include, url


from django.contrib import admin
admin.autodiscover()

from django.conf import settings

urlpatterns = patterns('',

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    #index
    url(r'^$','index.view.index',name='index'),
    url(r'^index/$', include('index.urls')),

    #store
#    url(r'^store/(?P<id>\b+)','index.view.store'),

    #account pages
    url(r'^accounts/', include("accounts.urls")),

    #goods
    url(r'^goods/',include('car.urls')),


    #static items
    url(r'^static/(?P<path>.*)$','django.views.static.serve',{'static_root':settings.STATIC_ROOT}),

    #errors
    url(r'^404$','index.view.err_404',name="404"),
)
