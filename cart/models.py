from django.db import models
from home.models import Product, User, Variant
from django.forms import ModelForm


class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    variant = models.ForeignKey(Variant, on_delete=models.CASCADE, blank=True, null=True)
    quantity = models.IntegerField()

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'سبد خرید'
        verbose_name_plural = 'سبد خرید ها'


class CartForm(ModelForm):
    class Meta:
        model = Cart
        fields = ['quantity']


class Compare(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    sessionkey = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self):
        return self.product.name


class CompareForm(ModelForm):
    class Meta:
        model = Compare
        fields = ['product']
