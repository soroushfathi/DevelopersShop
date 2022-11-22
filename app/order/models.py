from django.db import models
from django.contrib.auth.models import User
from home.models import Product, Variant
from django.core.validators import MinLengthValidator
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django_jalali.db import models as jmodels


def validate_postalcode(value):
    flags = [len(value) != 10, '3' in value, '5' in value]
    if all(flags):
        raise ValidationError(
            _('%(value)s is not an valid postalcode'),
            params={'value': value},
        )


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    create = jmodels.jDateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)
    codeorder = models.CharField(max_length=200, null=True)
    email = models.EmailField(blank=True, null=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=1000)
    postal_code = models.CharField(max_length=10, validators=[validate_postalcode], blank=True, null=True)
    totalprice = models.PositiveIntegerField(blank=True, null=True)
    discount = models.PositiveIntegerField(blank=True, null=True, default=0)

    def price(self):
        if self.discount is not None:
            return sum(x.item_price() for x in self.items.all()) * (100 - self.discount)//100
        else:
            return sum(x.item_price() for x in self.items.all())

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'سفارش'
        verbose_name_plural = 'سفارشات'


class ItemOrder(models.Model):
    # related name: connect from order to theire items
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    # cart informations
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    variant = models.ForeignKey(Variant, on_delete=models.CASCADE, blank=True, null=True)
    quantity = models.IntegerField()

    def __str__(self):
        return self.product.name

    def size(self):
        return self.variant.size.name

    def color(self):
        return self.variant.color.name

    def item_price(self):
        totalprice = 0
        if self.product.status != 'None':
            totalprice += self.variant.total_price * self.quantity
        else:
            totalprice += self.product.total_price * self.quantity
        return totalprice

    class Meta:
        verbose_name = 'محصول سفارش'
        verbose_name_plural = 'محصولات سفارش'


class Coupon(models.Model):
    code = models.CharField(max_length=20, unique=True)
    start = jmodels.jDateTimeField()
    end = jmodels.jDateTimeField()
    active = models.BooleanField()
    discount = models.PositiveIntegerField()

    class Meta:
        verbose_name = 'کد تخفیف'
        verbose_name_plural = 'کدهای تخفیف'
