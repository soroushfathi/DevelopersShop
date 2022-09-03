from django.shortcuts import render, redirect
from home.models import Product
from .models import Cart, CartForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from order.forms import OrderForm


def cart_detail(request):
    carts = Cart.objects.filter(user_id=request.user.id)
    user = request.user
    prof = request.user.profile
    total = 0
    for cart in carts:
        if cart.product.status != 'None':
            total += cart.variant.total_price * cart.quantity
        else:
            total += cart.product.total_price * cart.quantity
    orderform = OrderForm()
    context = {
        'carts': carts,
        'total': total,
        'orderform': orderform,
        'user': user, 'prof': prof,
    }
    return render(request, 'cart/cart.html', context=context)


@login_required(login_url='account:login')
def add_cart(request, pid):
    url = request.META.get('HTTP_REFERER')
    product = Product.objects.get(id=pid)
    var_id = None
    '''
    check if cart have been added
        - if cart has variant, we have to find product by variant id
        - if cart has not variant, we have to find product by product id
    '''
    if product.status != 'None':
        var_id = request.POST.get('varid')
        cart = Cart.objects.filter(user_id=request.user.id, variant_id=var_id)
        if cart:
            # same product(with same variant) have been added, so we increase quantity
            flag = True
        else:
            flag = False
    else:
        cart = Cart.objects.filter(user_id=request.user.id, product_id=pid)
        if cart:
            # same product have been added, so we increase quantity
            flag = True
        else:
            flag = False

    if request.method == 'POST':
        form = CartForm(request.POST)
        if form.is_valid():
            quan = form.cleaned_data['quantity']
            if flag:
                if product.status != 'None':
                    getcart = Cart.objects.get(user_id=request.user.id, product_id=pid, variant_id=var_id)
                    if getcart.variant.amount >= getcart.quantity + quan > 0:
                        getcart.quantity += quan
                    elif getcart.quantity + quan > getcart.variant.amount:
                        messages.error(request, 'درخواست بیش از حد موجودی است', 'danger')
                    elif getcart.quantity + quan <= 0:
                        messages.error(request, 'کمتر از یک عدد نامعتبر', 'danger')
                else:
                    getcart = Cart.objects.get(user_id=request.user.id, product_id=pid)
                    if getcart.product.amount >= getcart.quantity + quan > 0:
                        getcart.quantity += quan
                    elif getcart.quantity + quan > getcart.product.amount:
                        messages.error(request, 'درخواست بیش از حد موجودی است', 'danger')
                    elif getcart.product + quan <= 0:
                        messages.error(request, 'حداقل تعداد باید یکی باشد', 'danger')
                getcart.save()
            else:
                Cart.objects.create(product_id=pid, user_id=request.user.id, variant_id=var_id, quantity=quan)
                messages.success(request, '{} تعداد از این محصول با موفقیت به سبد خرید اضافه شد'.format(quan), 'success')
        return redirect(url)
    else:
        messages.error(request, 'دست نکن بچه :)', 'danger')


@login_required(login_url='account:login')
def remove_cart(request, cid):
    url = request.META.get('HTTP_REFERER')
    Cart.objects.filter(id=cid).delete()
    return redirect(url)


def compare(request, pid):
    if request.user.is_anonymous:
        pass
    else:
        pass
