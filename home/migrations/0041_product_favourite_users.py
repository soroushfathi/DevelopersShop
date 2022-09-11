# Generated by Django 4.0 on 2022-09-11 06:42

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0040_remove_product_favourite_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='favourite_users',
            field=models.ManyToManyField(blank=True, related_name='favourits', through='home.Favourite', to=settings.AUTH_USER_MODEL),
        ),
    ]
