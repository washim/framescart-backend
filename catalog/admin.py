from django.contrib import admin
from .models import Product, ProductAttribute, ProductAttributeItem, ProductOption, ProductImage
from billing.admin import StockInInline
from bracket.admin import CategoryInline

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

class ProductOptionInline(admin.TabularInline):
    model = ProductOption
    extra = 1

class ProductAttributeItemInline(admin.TabularInline):
    model = ProductAttributeItem
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline, CategoryInline, ProductOptionInline, StockInInline, ]

@admin.register(ProductAttribute)
class ProductAttributeAdmin(admin.ModelAdmin):
    inlines = [ProductAttributeItemInline, ]

@admin.register(ProductAttributeItem)
class ProductAttributeItemAdmin(admin.ModelAdmin):
    pass

@admin.register(ProductOption)
class ProductOptionAdmin(admin.ModelAdmin):
    pass

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    pass