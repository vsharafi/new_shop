from django.contrib import admin
from .models import Product, Comment
from jalali_date.admin import ModelAdminJalaliMixin


class CommentTabularInline(admin.TabularInline):
    model = Comment
    fields = ['text', 'author', 'stars', 'active']
    extra = 1


@admin.register(Product)
class ProductAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    model = Product
    list_display = ('title', 'description', 'datetime_created', 'datetime_modified', 'price', 'active',
                    'image', 'id')
    inlines = [
        CommentTabularInline,
    ]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    model = Comment
    list_display = ('text','product', 'author', 'datetime_created', 'stars', 'active', 'id')
