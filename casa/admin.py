from django.contrib import admin
from .models import CakeCategory, CakeProduct

# Register your models here.


@admin.register(CakeCategory)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(CakeProduct)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['cake_name', 'slug', 'price','available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('cake_name',)}