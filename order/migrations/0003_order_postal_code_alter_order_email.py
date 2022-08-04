# Generated by Django 4.0 on 2022-08-01 11:23

from django.db import migrations, models
import order.models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_rename_qunatity_itemorder_quantity_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='postal_code',
            field=models.CharField(blank=True, max_length=10, null=True, validators=[order.models.validate_postalcode]),
        ),
        migrations.AlterField(
            model_name='order',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
