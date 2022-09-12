# Generated by Django 4.0 on 2022-08-12 20:10

from django.db import migrations
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0025_alter_color_options_alter_comment_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'دسته بندی', 'verbose_name_plural': 'دسته بندی ها'},
        ),
        migrations.AlterField(
            model_name='category',
            name='created',
            field=django_jalali.db.models.jDateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='update',
            field=django_jalali.db.models.jDateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='create',
            field=django_jalali.db.models.jDateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='create',
            field=django_jalali.db.models.jDateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='update',
            field=django_jalali.db.models.jDateTimeField(auto_now=True),
        ),
    ]