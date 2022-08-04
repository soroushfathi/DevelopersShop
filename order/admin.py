from django.contrib import admin
from .models import Order, ItemOrder


class ItemOrderInline(admin.TabularInline):
    model = ItemOrder
    readonly_fields = ['user', 'product', 'variant', 'size', 'color', 'quantity', 'item_price']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'email', 'last_name', 'address', 'create', 'price', 'paid']
    inlines = [ItemOrderInline]


admin.site.register(Order, OrderAdmin)
admin.site.register(ItemOrder)
