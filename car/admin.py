#coding=latin1
from django.contrib import admin
from car.models import Items,Stores,Messages,Sorts
from mptt.admin import MPTTModelAdmin

class ItemsAdmin(admin.ModelAdmin):
    list_display = ('it_name','version','exit_date')
    search_fields = ('it_name','company','series')

class StoresAdmin(admin.ModelAdmin):
    list_display = ('st_name','tele')
    search_fields = ('st_name','it_description')

admin.site.register(Items,ItemsAdmin)
admin.site.register(Stores,StoresAdmin)
admin.site.register(Messages)
admin.site.register(Sorts,MPTTModelAdmin)