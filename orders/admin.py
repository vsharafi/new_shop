from django.contrib import admin
from .models import Order, OrderItem



class OrderItemTabularInline(admin.TabularInline):
    model = OrderItem
    fields = ['order', 'product', 'quantity', 'price']
    # extra = 1


@admin.register(Order)
class ProductAdmin(admin.ModelAdmin):
    model = Order
    list_display = ('user', 'first_name', 'last_name', 'phone_number', 'address', 'is_paid',
                    'datetime_created', 'datetime_modified', 'order_note', 'id')
    inlines = [
        OrderItemTabularInline,
    ]


@admin.register(OrderItem)
class CommentAdmin(admin.ModelAdmin):
    model = OrderItem
    list_display = ('order','product', 'quantity', 'price', 'id')
