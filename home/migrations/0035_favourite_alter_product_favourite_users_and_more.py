# Generated by Django 4.0 on 2022-09-11 05:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0034_alter_product_views_view'),
    ]

    operations = [

    ]