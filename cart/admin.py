from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(CartList)

class ItemsAdmin(admin.ModelAdmin):
    list_display = ['products', 'cart', 'quantity', 'active']
admin.site.register(Items,ItemsAdmin)
