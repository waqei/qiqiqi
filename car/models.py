#coding=utf-8
from django.db import models

class Items(models.Model):
    it_name=models.CharField(max_length=10,verbose_name='商品名称')
    company=models.CharField(max_length=20,verbose_name='所属商铺')
    series=models.CharField(max_length=10,verbose_name='系列')
    version=models.CharField(max_length=30,verbose_name='型号')
    description=models.CharField(max_length=200,verbose_name='描述')
    exit_date=models.DateField(verbose_name='上市时间',blank=True)
    price=models.CharField(max_length=20,verbose_name='价格')
    def __unicode__(self):
        return self.it_name

class Stores(models.Model):
    st_name=models.CharField(max_length=10,verbose_name='商铺名称')
    address=models.CharField(max_length=30,verbose_name='地址')
    tele=models.CharField(max_length=12,verbose_name='联系电话')
    it_description=models.CharField(max_length=200,verbose_name='商铺描述')
    email=models.EmailField('e-mail',blank=True)
    def __unicode__(self):
        return self.st_name

class Messages(models.Model):
    mes_store=models.CharField(max_length=10)
    contact_number=models.CharField(max_length=12,verbose_name='您的联系电话')
    content=models.CharField(max_length=200,verbose_name='留言内容')
    def __unicode__(self):
        return self.contact_number


# Create your models here.
