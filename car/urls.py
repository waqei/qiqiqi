#coding=utf-8
from django.conf.urls import patterns, url
from car.models import Links,Sorts,Items

urlpatterns = patterns('',
    ##item
    url(r'^item/add/(?P<muser>\w+)/','car.views.addItems',name="add_items"),
    url(r'^item/manage/$','car.views.manageitems',name="manage_items"),
    url(r'^item/manage/dele/(?P<id>\b.)/$','car.views.dele',{'model':Items},name="dele_items",),

    ##sort&&brand
    url(r'^show_sort/$','car.views.show_sort',name="show_sort"),
    url(r'^show_sort/add/(?P<parent>\w.*)/$','car.views.add_sort',name="add_sort"),
    url(r'^show_sort/dele/(?P<id>\w.*)/$','car.views.dele',{'model':Sorts},name="dele_sort"),

    ##store
    url(r'^store/add','car.views.addStore',name="add_store"),

    ##ad
    url(r'^ad/','car.views.ad',name='ad_manage'),

    ##links
    url(r'^links/$','car.views.links',name='links'),
    url(r'^links/dele/(?P<id>\w.*)/$','car.views.dele',{'model':Links})
)