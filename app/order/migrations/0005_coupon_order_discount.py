# Generated by Django 4.0 on 2022-08-04 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_order_totalprice'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20, unique=True)),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('active', models.BooleanField()),
                ('discount', models.PositiveIntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='discount',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
