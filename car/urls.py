#coding=utf-8
from django.conf.urls import patterns, include, url



urlpatterns = patterns('',

    ##item
    url(r'^item/add/(?P<muser>\w+)/','car.views.addItems',name="add_items"),
    url(r'^item/manage','car.views.manageitems',name="manage_items"),

    ##sort&&brand
    url(r'^show_sort/$','car.views.show_sort',name="show_sort"),
    url(r'^show_sort/add/(?P<parent>\w.*)/$','car.views.add_sort',name="add_sort"),
    url(r'^show_sort/dele/(?P<id>\w.*)/$','car.views.dele_sort',name="dele_sort"),

#    url(r'^add_brand/$','car.views.addbrand',name="add_brand"),
#    url(r'^add_brand/dele/(?P<id>\w.*)$','car.views.delebrand',name="dele_brand"),


    ##store
    url(r'^store/add','car.views.addStore',name="add_store"),

    ##ad
    url(r'^ad/','car.views.ad',name='ad_manage'),

    ##links
    url(r'links/','car.views.links',name='m_links'),
    url(r'links/dele/(?P<id>\b.*)/$','car.views.dele_link'),

)