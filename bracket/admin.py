from django.contrib import admin
from .models import Category, CategoryItem

class CategoryInline(admin.TabularInline):
    model = Category
    extra = 1

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(CategoryItem)
class CategoryItemAdmin(admin.ModelAdmin):
    pass
