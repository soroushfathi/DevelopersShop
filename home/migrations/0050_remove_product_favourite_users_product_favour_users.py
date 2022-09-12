# Generated by Django 4.0 on 2022-09-11 11:25

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0049_rename_favourite_users_product_fav_users'),
    ]

    operations = [
        # migrations.RemoveField(
        #     model_name='product',
        #     name='favourite_users',
        # ),
        migrations.AddField(
            model_name='product',
            name='favour_users',
            field=models.ManyToManyField(blank=True, related_name='favourits', to=settings.AUTH_USER_MODEL),
        ),
    ]