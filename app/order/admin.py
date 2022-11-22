from django.contrib import admin
from .models import Order, ItemOrder, Coupon
from django_jalali.admin.filters import JDateFieldListFilter


class ItemOrderInline(admin.TabularInline):
    model = ItemOrder
    readonly_fields = ['user', 'product', 'variant', 'size', 'color', 'quantity', 'item_price']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'codeorder', 'email', 'last_name', 'address', 'create', 'price', 'paid']
    inlines = [ItemOrderInline]
    list_filter = (
        ('create', JDateFieldListFilter),
    )


class CouponAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Coupon._meta.get_fields()]
    list_editable = ['end']
    list_filter = (
        ('code', JDateFieldListFilter),
    )


admin.site.register(Order, OrderAdmin)
admin.site.register(ItemOrder)
admin.site.register(Coupon, CouponAdmin)
