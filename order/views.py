from django.shortcuts import render, redirect
from .forms import OrderForm
from django.contrib import messages
from .models import Order, ItemOrder
from cart.models import Cart


def order_detail(request):
    orders = Order.objects.filter(user_id=request.user.id)
    return render(request, 'order/detail.html', context={'orders': orders})


def create_order(request):
    orderform = OrderForm()

    if request.method == 'POST' or None:
        orderform = OrderForm(request.POST)
        if orderform.is_valid():
            data = orderform.cleaned_data
            totalprice = 0
            carts = Cart.objects.filter(user_id=request.user.id)
            for cart in carts:
                if cart.product.status != 'None':
                    totalprice += cart.variant.total_price * cart.quantity
                else:
                    totalprice += cart.product.total_price * cart.quantity
            order = Order.objects.create(
                user_id=request.user.id, first_name=data['first_name'], last_name=data['last_name'],
                email=data['email'], address=data['address'], postal_code=data['postal_code'], totalprice=totalprice,
            )
            orderitems = []
            for cart in carts:
                orderitems.append(ItemOrder.objects.create(
                    order_id=order.id, user_id=request.user.id,
                    product_id=cart.product.id, variant_id=cart.variant.id, quantity=cart.quantity,
                ))
            return redirect('order:detail')
        else:
            return render(request, 'order/create.html', context={'orderform': orderform})

    return render(request, 'order/create.html', context={'orderform': orderform})
