# Generated by Django 4.0 on 2022-08-12 19:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0005_remove_cart_order'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cart',
            options={'verbose_name': 'سبد خرید', 'verbose_name_plural': 'سبد خرید ها'},
        ),
    ]
