from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ('title', 'description', 'datetime_created', 'datetime_modified', 'price', 'active', 'id')
