from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from django.contrib.admin import ModelAdmin

from . models import Category,Product

# Register your models here.
class BaseModelAdmin(ModelAdmin):
    # Custom behavior and options for all ModelAdmin subclasses
    pass
class CategoryAdmin(BaseModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Category,CategoryAdmin)


class ProductAdmin(ModelAdmin):
    list_display = ['name', 'price', 'stock', 'available', 'created', 'updated']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}
    list_per_page = 20
admin.site.register(Product, ProductAdmin)

