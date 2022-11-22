from django.contrib import admin
from .models import Category, Product, Variant, Size, Color, Comment, Images, Brand, PriceTracker, View


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created', 'update', 'sub_category')
    list_filter = ('created',)
    prepopulated_fields = {
        'slug': ('name', ),
    }


class ProductVariantInline(admin.TabularInline):
    model = Variant
    extra = 2


class ImageInlines(admin.TabularInline):
    model = Images
    extra = 2


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'create', 'update', 'amount', 'available', 'total_price', 'unit_price', 'discount')
    # fieldsets = (
    #     ('Price', {
    #         'fields': ('total_price', 'discount', 'unit_price'),
    #     }),
    # )
    list_filter = ('amount', 'unit_price', 'discount')
    list_editable = ('amount',)
    change_list_template = 'home/admin-panel-statics.html'
    # raw_id_fields = ('',)
    inlines = [ProductVariantInline, ImageInlines]


class SizeAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')


class ColorAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'comment')


class ViewsAdmin(admin.ModelAdmin):
    list_display = ('ip', 'product', 'create')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Size, SizeAdmin)
admin.site.register(Color, ColorAdmin)
admin.site.register(Brand)
admin.site.register(Variant)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Images)
admin.site.register(PriceTracker)
admin.site.register(View, ViewsAdmin)
