from django import forms
import django_filters
from .models import *


class ProductFilter(django_filters.FilterSet):
    price_from = django_filters.NumberFilter(field_name='unit_price', lookup_expr='gte')
    price_to = django_filters.NumberFilter(field_name='unit_price', lookup_expr='lte')
