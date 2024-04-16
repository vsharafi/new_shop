from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _



class Order(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='orders', verbose_name=_('User'))
    first_name = models.CharField(_('First Name'), max_length=100, )
    last_name = models.CharField(_('Last Name'), max_length=100, )
    phone_number = models.CharField(_('Phone Number'), max_length=150, )    
    address = models.CharField(_('Address'), max_length=700, )
    is_paid = models.BooleanField(_('Is Paid?'), default=False, )
    datetime_created = models.DateTimeField(_('Created'), auto_now_add=True, )
    datetime_modified = models.DateTimeField(_('Modified'), auto_now=True, )
    order_note = models.CharField(_('Order Note'), max_length=700, blank=True, )

    def __str__(self):
        return f'Oreder {self.id}'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE, related_name='order_items')
    quantity = models.PositiveIntegerField(default=1)
    price = models.PositiveIntegerField()

    def __str__(self):
        return f'Order item {self.id} for Order {self.order}'