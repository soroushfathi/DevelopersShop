from django.shortcuts import render, redirect
from .forms import OrderForm
from django.contrib import messages
from .models import Order, ItemOrder, Coupon
from cart.models import Cart
from .forms import CouponForm
from django.views.decorators.http import require_POST
from django.utils import timezone


def order_detail(request):
    orders = Order.objects.filter(user_id=request.user.id)
    couponform = CouponForm()
    return render(request, 'order/detail.html', context={'orders': orders, 'couponform': couponform})


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


@require_POST
def coupon(request, oid):
    form = CouponForm(request.POST)
    nowtime = timezone.now()
    if form.is_valid():
        code = form.cleaned_data['code']
        try:
            coupon = Coupon.objects.get(code__exact=code, start__lte=nowtime, end__gte=nowtime, active=True)
        except Coupon.DoesNotExist:
            messages.error(request, 'کد تخفیف نا معتبر', 'error')
            return redirect('order:detail')
        order = Order.objects.get(id=oid)
        order.discount = coupon.discount
        order.save()
    return redirect('order:detail')
