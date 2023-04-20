# Generated by Django 4.1.7 on 2023-04-03 06:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_remove_productattribute_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category_items', to='catalog.categoryitem'),
        ),
        migrations.AlterField(
            model_name='category',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='catalog.product'),
        ),
        migrations.CreateModel(
            name='ProductOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_options', to='catalog.product')),
                ('product_attribute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_option_items', to='catalog.productattribute')),
            ],
        ),
    ]
