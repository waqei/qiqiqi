#coding=utf-8
from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os,time,random



class Stores(models.Model):
    st_name=models.CharField(max_length=10,verbose_name='商铺名称')
    boss=models.OneToOneField(User,verbose_name='商铺主')
    sell=models.ManyToManyField(Classify,verbose_name='主营产品')
    address=models.CharField(max_length=30,verbose_name='地址')
    tele=models.CharField(max_length='11',verbose_name='联系电话')
    it_description=models.CharField(max_length=200,verbose_name='商铺描述')
    email=models.EmailField('e-mail',blank=True)
    def __unicode__(self):
        return self.st_name

class Items(models.Model):
    it_name=models.CharField(max_length=10,verbose_name='商品名称')
    company=models.ForeignKey(Stores,max_length=20,verbose_name='所属商铺')
    classify=models.ManyToManyField(Classifys,max_length=20,verbose_name='分类')
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


class ImageStorage(FileSystemStorage):
    from django.conf import settings
    def __init__(self, location=settings.MEDIA_ROOT, base_url=settings.MEDIA_URL):
        #初始化
        super(ImageStorage, self).__init__(location, base_url)
        #重写 _save方法
        def _save(self, name, content):
            #文件扩展名
            ext = os.path.splitext(name)[1]
            #文件目录
            d = os.path.dirname(name)
            #定义文件名，年月日时分秒随机数
            fn = time.strftime('%Y%m%d%H%M%S')
            fn = fn + '_%d' % random.randint(0,100)
            #重写合成文件名
            name = os.path.join(d, fn + ext)
            #调用父类方法
            return super(ImageStorage, self)._save(name, content)


class Messages(models.Model):
#    mes_store=models.CharField(max_length=10,verbose_name='')
    store=models.ForeignKey(Stores,verbose_name='商户名称')
    is_read=models.BooleanField()
    contact_number=models.DecimalField(max_digits='11',decimal_places='0',verbose_name='您的联系电话',help_text='请留下您的联系电话，方便工作人员与您联系，电话号码仅工作人员可见。')
    content=models.CharField(max_length=200,verbose_name='留言内容')
    def __unicode__(self):
        return self.contact_number

class Classifys:
    name=models.CharField(max_length=20,verbose_name="分类")


class Brands:
    name= models.CharField(max_length=20,verbose_name="品牌")
    image= models.ImageField(upload_to="brand",verbose_name="品牌标志")


# Create your models here.
