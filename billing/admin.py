from django import forms
from django.contrib import admin
from django.db import models
from .models import Invoice, StockIn, Stockout

class StockInInline(admin.TabularInline):
    model = StockIn
    extra = 1

class StockoutInline(admin.TabularInline):
    model = Stockout
    extra = 1
    formfield_overrides = {
        models.TextField: {
            'widget': forms.Textarea(attrs={'rows':'3', 'cols':'50'})
        }
    }

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    inlines = [StockoutInline, ]