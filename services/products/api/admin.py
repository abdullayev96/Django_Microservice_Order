from django.contrib import admin
from .models import *


class ProductAdmin(admin.ModelAdmin):
     list_display = ('id', 'name', 'price', 'description')
     list_filter = ('id', 'price', 'name')
     ordering = ('id',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category)