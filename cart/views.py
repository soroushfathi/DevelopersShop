from django.shortcuts import render, redirect
from home.models import Product
from .models import Cart, CartForm
from django.contrib import messages


def cart_detail(request):
    return render(request, 'cart/cart.html')


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
        var_id = request.POST.get('select')
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
                else:
                    getcart = Cart.objects.get(user_id=request.user.id, product_id=pid)
                getcart.quantity += quan
                getcart.save()
            else:
                Cart.objects.create(product_id=pid, user_id=request.user.id, variant_id=var_id, quantity=quan)
        return redirect(url)
    else:
        messages.error(request, 'دست نکن بچه :)', 'danger')


def remove_cart(request):
    pass
