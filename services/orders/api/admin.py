from django.contrib import admin
from .models import *


class OrderAdmin(admin.ModelAdmin):
     list_display = ('id', 'total', 'customer_name', 'customer_email')
     list_filter = ('id', 'customer_email')
     ordering = ('id',)


admin.site.register(Order, OrderAdmin)