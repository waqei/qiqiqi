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
    url(r'^index/', include('index.urls')),

    #store
    url(r'^store/(?P<store_id>\b.)/$','index.view.store'),
    url(r'^store/(?P<store_id>\b.*)/info.html$','index.view.storeInfo'),
    url(r'^store/(?P<store_id>\b.*)/classify/(?P<sort_id>\b.*).html/(?P<p>\b.*)$','index.view.classify_s'),
    url(r'^store/(?P<store_id>\b.*)/view/(?P<item_id>\b.*).html$','index.view.views'),
    url(r'^store/(?P<store_id>\b.*)/message.html$','index.view.message'),

    #comments
    url(r'^comments/', include('django.contrib.comments.urls')),
#    url(r'^comments/post/(\w.*)/$', 'index.view.comment_done')),


    #account pages
    url(r'^accounts/', include("accounts.urls")),

    #goods
    url(r'^goods/',include('car.urls')),


    #static items
    url(r'^static/(?P<path>.*)$','django.views.static.serve',{'static_root':settings.STATIC_ROOT}),

    #errors
    url(r'^404$','index.view.err_404',name="404"),
)
