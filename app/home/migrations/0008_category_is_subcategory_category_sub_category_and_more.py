# Generated by Django 4.0 on 2022-03-25 14:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_product_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='is_subcategory',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='category',
            name='sub_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub', to='home.category'),
        ),
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(blank=True, to='home.Category'),
        ),
    ]