#coding=utf-8
from django.db import models
from django.contrib.auth.models import User
#from django.core.files.storage import FileSystemStorage
#from django.conf import settings
#import os,time,random
from mptt.models import MPTTModel,TreeForeignKey

BOOLE_CHOICES=(
    ('是','1'),
    ('否','0'),
    )

#分类
class Sorts(MPTTModel):
    name=models.CharField(max_length=20,verbose_name="分类名称",unique=True)
    parent=TreeForeignKey("self", blank=True, null=True, related_name="children")


    class MPTTMeta:
        order_insertion_by = ['name']

    def __unicode__(self):
        return self.name


#品牌
class Brands(models.Model):
    name= models.CharField(max_length=20,verbose_name="品牌名称",unique=True)
    image= models.ImageField(verbose_name="品牌标志",upload_to="brand")

    def __unicode__(self):
        return self.name



#商铺
class Stores(models.Model):
    boss=models.OneToOneField(User,verbose_name='商铺主')
    st_name=models.CharField(max_length=10,verbose_name='商铺名称',unique=True)
    tele=models.CharField(max_length=11,verbose_name='联系电话')
    fax=models.CharField(max_length=11,verbose_name='传真',blank=True)
    sell=models.ManyToManyField(Sorts,max_length=100,verbose_name='主营产品')
    s_brand=models.ManyToManyField(Brands,max_length=100,verbose_name='主营品牌')
    it_description=models.CharField(max_length=200,verbose_name='商铺描述')
    address=models.CharField(max_length=30,verbose_name='地址')

    def __unicode__(self):
        return self.st_name


#商品
class Items(models.Model):
    it_name=models.CharField(max_length=10,verbose_name='商品名称')
    company=models.ForeignKey(Stores,max_length=20,verbose_name='所属商铺')
    sort=models.ManyToManyField(Sorts,verbose_name='分类')
    brand=models.ManyToManyField(Brands,max_length=10,verbose_name='品牌',blank=True)
    version=models.CharField(max_length=30,verbose_name='型号',blank=True)
    description=models.CharField(max_length=200,verbose_name='描述')
    exit_date=models.DateField(verbose_name='上市时间',blank=True)
    price=models.CharField(max_length=20,verbose_name='价格')
    img=models.ImageField(verbose_name='商品图片',upload_to='image',blank=True)

    def get_company(self):
        return self.company

    def __unicode__(self):
        return self.it_name



#留言
class Messages(models.Model):
    store=models.ForeignKey(Stores,verbose_name='商户名称',unique=True)
    is_read=models.BooleanField(max_length='5',choices=BOOLE_CHOICES)
    contact_number=models.DecimalField(max_digits='11',decimal_places='0',verbose_name='您的联系电话',help_text='请留下您的联系电话，方便工作人员与您联系，电话号码仅工作人员可见。')
    content=models.CharField(max_length=200,verbose_name='留言内容')
    def __unicode__(self):
        return self.contact_number


class Ads(models.Model):
    loc1=models.ImageField(verbose_name='首页小图1',upload_to="ad")
    loc2=models.ImageField(verbose_name='首页小图2',upload_to="ad")
    loc3=models.ImageField(verbose_name='首页小图3',upload_to="ad")
    loc4=models.ImageField(verbose_name='首页小图4',upload_to="ad")
    loc5=models.ImageField(verbose_name='首页小图5',upload_to="ad")


class Links(models.Model):
    site=models.CharField(max_length=10,verbose_name='站点名称',)
    url=models.URLField(verbose_name='站点网址',max_length=64)