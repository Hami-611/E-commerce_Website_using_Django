# Generated by Django 5.1.4 on 2024-12-26 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_order_orderitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='order',
            name='pincode',
            field=models.CharField(max_length=7),
        ),
    ]
