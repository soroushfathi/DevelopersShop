# Generated by Django 4.0 on 2022-08-12 20:10

from django.db import migrations
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0007_alter_coupon_options_alter_itemorder_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='end',
            field=django_jalali.db.models.jDateTimeField(),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='start',
            field=django_jalali.db.models.jDateTimeField(),
        ),
        migrations.AlterField(
            model_name='order',
            name='create',
            field=django_jalali.db.models.jDateTimeField(auto_now_add=True),
        ),
    ]
