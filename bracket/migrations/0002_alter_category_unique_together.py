# Generated by Django 4.1.7 on 2023-04-06 05:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_alter_productoption_unique_together'),
        ('bracket', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='category',
            unique_together={('product', 'category_item')},
        ),
    ]