# Generated by Django 4.1.7 on 2023-04-06 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0002_stockout_product_attribute_item_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockout',
            name='product_attribute_item',
            field=models.TextField(blank=True, null=True),
        ),
    ]
