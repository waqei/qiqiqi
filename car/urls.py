#coding=utf-8
from django.conf.urls import patterns, url
from car.models import Links,Sorts,Items,News
from form import Ad6Form,AdmiddleForm

urlpatterns = patterns('',
    ##item
    url(r'^item/add/$','car.views.addItems',name="add_items"),
    url(r'^item/manage/$','car.views.manageitems',name="manage_items"),
    url(r'^item/manage/dele/(?P<id>\b.)/$','car.views.dele',{'model':Items},name="dele_items",),

    ##sort&&brand
    url(r'^show_sort/$','car.views.show_sort',name="show_sort"),
    url(r'^show_sort/add/(?P<parent>\w.*)/$','car.views.add_sort',name="add_sort"),
    url(r'^show_sort/dele/(?P<id>\w.*)/$','car.views.dele',{'model':Sorts},name="dele_sort"),

    ##store
    url(r'^store/add/$','car.views.addStore',name="add_store"),
    url(r'^store/$','car.views.showStoreinfo',name="show_store_info"),
    url(r'^store/edit/$','car.views.editStore',name="edit_store_info"),
    url(r'^store/edit/ad/$','car.views.storeAd',name="edit_store_ad"),

    ##ad
    url(r'^ad/$','car.views.ad',name='ad_manage'),
    url(r'^ad/ad6/$','car.views.ad_m',{'Form':Ad6Form},name='ad_6'),
    url(r'^ad/admiddle/$','car.views.ad_m',{'Form':AdmiddleForm},name='ad_middle'),

    ##links
    url(r'^links/$','car.views.links',name='links'),
    url(r'^links/dele/(?P<id>\w.*)/$','car.views.dele',{'model':Links}),

    ##news
    url(r'^news/$','car.views.news',name='news'),
    url(r'^news/dele/(?P<id>\b.*)/$','car.views.dele',{'model':News}),
)