#encoding = utf-8

from django.http import HttpResponse
import ImageFile
from accounts.forms import ItemsForm

def addPicture(request):
    """
    上传图片
    """
    if request.method == 'POST':
        form = ItemsForm(request.POST,request.FILES)
        if form.is_valid():
            f=request.FILES["imagefile"]
            parser=ImageFile.Parser()
            for chunk in f.chunks():
                paser.feed(chunk)
            img = parser.close()
            img.save("/templates/static/image")