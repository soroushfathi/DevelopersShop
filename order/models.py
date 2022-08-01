from django.db import models
from django.contrib.auth.models import User
from home.models import Product, Variant
from django.core.validators import MinLengthValidator
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_postalcode(value):
    flags = [len(value) != 10, '3' in value, '5' in value]
    if all(flags):
        raise ValidationError(
            _('%(value)s is not an valid postalcode'),
            params={'value': value},
        )


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    create = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)
    email = models.EmailField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=1000)
    postal_code = models.CharField(max_length=10, validators=[validate_postalcode])

    def __str__(self):
        return self.user.username


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
