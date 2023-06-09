# Generated by Django 4.1.7 on 2023-04-03 05:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField()),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField()),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('product_type', models.CharField(choices=[('border_frame', 'Border Frame'), ('canvas_frame', 'Canvas Frame'), ('tshirt', 'Tshirt')], default='canvas_frame', max_length=50)),
                ('base_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('mrp', models.DecimalField(decimal_places=2, max_digits=6)),
                ('selling_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Create Date')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Modified Date')),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='ProductAttribute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_attributes', to='catalog.product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='uploads')),
                ('caption', models.CharField(blank=True, max_length=255, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_images', to='catalog.product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductAttributeItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('base_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('selling_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('quantity', models.IntegerField(default=1)),
                ('product_attribute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_attribute_items', to='catalog.productattribute')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='catalog.categoryitem')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='catalog.product')),
            ],
        ),
    ]
