from django.contrib import admin

from apitest.admin import ApitestAdmin
from apitest.models import Apis, Apitest
from product.models import Product
# Register your models here.


class ApitestAdmin(admin.TabularInline):
    list_display = ['apitestname', 'apitester', 'apitestresult', 'create_time', 'id', 'product']
    model = Apitest
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    list_display = ['productname', 'productdesc', 'producter', 'create_time', 'id']
    inlines = [ApitestAdmin]


class ApisAdmin(admin.TabularInline):
    list_display = ['apiname', 'apiurl', 'apiparamvalue', 'apimethod', 'apiresult', 'apistatus', 'create_time', 'id',
                    'product']
    model = Apis
    extra = 1


admin.site.register(Product, ProductAdmin)

