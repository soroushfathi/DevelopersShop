# Generated by Django 4.0 on 2022-03-23 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='information',
            field=models.TextField(blank=True, null=True),
        ),
    ]
