# Generated by Django 4.0 on 2022-07-24 18:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0023_alter_comment_like_images'),
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='variant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.variant'),
        ),
    ]
