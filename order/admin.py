from django.contrib import admin
from .models import Order, ItemOrder, Coupon


class ItemOrderInline(admin.TabularInline):
    model = ItemOrder
    readonly_fields = ['user', 'product', 'variant', 'size', 'color', 'quantity', 'item_price']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'email', 'last_name', 'address', 'create', 'price', 'paid']
    inlines = [ItemOrderInline]


class CouponAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Coupon._meta.get_fields()]
    list_editable = ['end']


admin.site.register(Order, OrderAdmin)
admin.site.register(ItemOrder)
admin.site.register(Coupon, CouponAdmin)
