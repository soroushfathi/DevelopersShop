from django import forms
import django_filters
from . import models


class ProductFilter(django_filters.FilterSet):
    Choice1 = {
        ('گران ترین', 'گران ترین'),
        ('ارزان ترین', 'ارزان ترین'),
    }

    Choice2 = {
        ('جدید ترین', 'جدید ترین'),
    }

    Choice3 = {
        ('با تخفیف ترین', 'با تخفیف ترین'),
    }

    Choice4 = {
        ('محبوب ترین', 'محبوب ترین'),
    }
    price_from = django_filters.NumberFilter(field_name='unit_price', lookup_expr='gte')
    price_to = django_filters.NumberFilter(field_name='unit_price', lookup_expr='lte')
    size = django_filters.ModelMultipleChoiceFilter(queryset=models.Size.objects.all(), widget=forms.CheckboxSelectMultiple)
    color = django_filters.ModelMultipleChoiceFilter(queryset=models.Color.objects.all(), widget=forms.CheckboxSelectMultiple)
    priceorder = django_filters.ChoiceFilter(choices=Choice1, method='priceorder_filter')
    timeorder = django_filters.ChoiceFilter(choices=Choice2, method='timeorder_filter')
    discountorder = django_filters.ChoiceFilter(choices=Choice3, method='discountorder_filter')
    # todo sellcount: add sell count (order view, + sell field in product model)
    favourite = django_filters.ChoiceFilter(choices=Choice4, method='favourite_filter')

    def priceorder_filter(self, queryset, name, value):
        pord = 'unit_price' if value == 'ارزان ترین' else '-unit_price'
        return queryset.order_by(pord)

    def timeorder_filter(self, queryset, name, value):
        tord = '-create' if value == 'جدید ترین' else 'create'
        return queryset.order_by(tord)

    def discountorder_filter(self, queryset, name, value):
        dord = '-discount' if value == 'با تخفیف ترین' else 'discount'
        return queryset.order_by(dord)

    def favourite_filter(self, queryset, name, value):
        ford = '-favcount' if value == 'محبوب ترین' else 'favcount'
        return queryset.order_by(ford)
