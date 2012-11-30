#coding=utf-8
from django.db import models
from django.contrib.auth.models import User
#from django.core.files.storage import FileSystemStorage
#from django.conf import settings
#import os,time,random

BOOLE_CHOICES=(
    ('是','1'),
    ('否','0'),
    )

#分类
class Sorts(models.Model):
    name=models.CharField(max_length=20,verbose_name="分类名称",unique=True)

    def __unicode__(self):
        return self.name


#品牌
class Brands(models.Model):
    name= models.CharField(max_length=20,verbose_name="品牌名称",unique=True)
    image= models.ImageField(upload_to="brand",verbose_name="品牌标志",blank=True)

    def __unicode__(self):
        return self.name



#商铺
class Stores(models.Model):
    st_name=models.CharField(max_length=10,verbose_name='商铺名称',unique=True)
    boss=models.OneToOneField(User,verbose_name='商铺主')
    sell=models.ManyToManyField(Sorts,verbose_name='主营产品',help_text="按下Ctrl键支持多选")
    s_brand=models.ManyToManyField(Brands,verbose_name='主营品牌',help_text="按下Ctrl键支持多选")
    address=models.CharField(max_length=30,verbose_name='地址')
    tele=models.CharField(max_length='11',verbose_name='联系电话')
    it_description=models.CharField(max_length=200,verbose_name='商铺描述')
    email=models.EmailField('e-mail',blank=True)
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
#    mes_store=models.CharField(max_length=10,verbose_name='')
    store=models.ForeignKey(Stores,verbose_name='商户名称',unique=True)
    is_read=models.BooleanField(max_length='5',choices=BOOLE_CHOICES)
    contact_number=models.DecimalField(max_digits='11',decimal_places='0',verbose_name='您的联系电话',help_text='请留下您的联系电话，方便工作人员与您联系，电话号码仅工作人员可见。')
    content=models.CharField(max_length=200,verbose_name='留言内容')
    def __unicode__(self):
        return self.contact_number


#中间model
class Middle(models.Model):
    sort=models.ForeignKey(Items)
    Items=models.ForeignKey(Sorts)

# Create your models here.
