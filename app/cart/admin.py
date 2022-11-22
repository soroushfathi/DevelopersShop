from django.contrib import admin
from .models import Cart, Compare


class CartAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'variant', 'quantity']


class CompareAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'sessionkey']


admin.site.register(Cart, CartAdmin)
admin.site.register(Compare, CompareAdmin)
