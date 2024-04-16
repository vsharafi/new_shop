from django.shortcuts import render, redirect
from .forms import OrderForm
from django.contrib.auth.decorators import login_required
from .models import Order, OrderItem
from cart.cart import Cart
from django.contrib import messages
from django.utils.translation import gettext as _



@login_required
def order_create_view(request):
    cart = Cart(request)
    form = OrderForm()

    if len(cart) == 0:
        messages.warning(request, _('Your cart is empty. Please add some product to your cart.'))
        return redirect('product_list')

    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()

            for item in cart:
                OrderItem.objects.create(order=obj,
                                        product = item['product_obj'],
                                        quantity = item['quantity'],
                                        price= item['product_obj'].price)
                
            cart.clear()

            request.user.first_name = obj.first_name
            request.user.last_name = obj.last_name
            request.user.phone_number = obj.phone_number
            request.user.save()
            messages.success(request, _('Your order has been successfully placed.'))


    return render(request, 'orders/order_create.html', {'form':form})