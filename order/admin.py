from django.contrib import admin
from .models import Order, ItemOrder


class ItemOrderInline(admin.TabularInline):
    model = ItemOrder
    readonly_fields = ['user', 'product', 'variant', 'quantity']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'email', 'last_name', 'address', 'create', 'paid']
    inlines = [ItemOrderInline]


admin.site.register(Order, OrderAdmin)
admin.site.register(ItemOrder)
