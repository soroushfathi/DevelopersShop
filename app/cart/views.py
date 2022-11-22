from django.shortcuts import render, redirect, get_object_or_404
from home.models import Product, Variant
from .models import Cart, CartForm, Compare
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from order.forms import OrderForm
from django.views.decorators.http import require_POST
from django.http import JsonResponse


def cart_detail(request):
    total = 0
    if request.user.is_authenticated:
        carts = Cart.objects.filter(user_id=request.user.id)
        user = request.user
        prof = request.user.profile
        for cart in carts:
            if cart.product.status != 'None':
                total += cart.variant.total_price * cart.quantity
            else:
                total += cart.product.total_price * cart.quantity
        orderform = OrderForm()
        context = {'carts': carts, 'total': total, 'orderform': orderform, 'user': user, 'prof': prof}
        return render(request, 'cart/cart.html', context=context)
    else:
        carts = Cart.objects.filter(user=None, sessionkey=request.session.session_key)
        if carts.exists():
            for cart in carts:
                if cart.product.status != 'None':
                    total += cart.variant.total_price * cart.quantity
                else:
                    total += cart.product.total_price * cart.quantity
        context = {'carts': carts, 'total': total}
        return render(request, 'cart/cart.html', context=context)


def add_cart(request, pid):
    url = request.META.get('HTTP_REFERER')
    product = Product.objects.get(id=pid)
    var_id = None
    '''
    check if cart have been added
        - if cart has variant, we have to find product by variant id
        - if cart has not variant, we have to find product by product id
    '''
    is_auth = request.user.is_authenticated
    session_key = request.session.session_key
    user_id = request.user.id
    # if cart exist: same product(with same variant) have been added, so we increase quantity
    if product.status != 'None':
        var_id = request.POST.get('varid')
        cart = Cart.objects.filter(user_id=user_id if is_auth else None, variant_id=var_id, sessionkey=session_key if not is_auth else None)
        flag = True if cart.exists() else False
    else:
        cart = Cart.objects.filter(user_id=user_id if is_auth else None, product_id=pid, sessionkey=session_key if not is_auth else None)
        flag = True if cart.exists() else False

    form = CartForm(request.POST)
    if form.is_valid():
        quan = form.cleaned_data['quantity']
        if flag:
            if product.status != 'None':
                getcart = Cart.objects.get(user_id=user_id if is_auth else None, product_id=pid, variant_id=var_id, sessionkey=session_key if not is_auth else None)
                if getcart.variant.amount >= getcart.quantity + quan > 0:
                    getcart.quantity += quan
                elif getcart.quantity + quan > getcart.variant.amount:
                    messages.error(request, 'درخواست بیش از حد موجودی است.', 'danger')
                elif getcart.quantity + quan <= 0:
                    messages.error(request, 'تعداد محصول نمیتواند کمتر از 1 باشد.', 'danger')
            else:
                getcart = Cart.objects.get(user_id=user_id if is_auth else None, product_id=pid, sessionkey=session_key if not is_auth else None)
                if getcart.product.amount >= getcart.quantity + quan > 0:
                    getcart.quantity += quan
                elif getcart.quantity + quan > getcart.product.amount:
                    messages.error(request, 'درخواست بیش از حد موجودی است.', 'danger')
                elif getcart.product + quan <= 0:
                    messages.error(request, 'تعداد محصول نمیتواند کمتر از 1 باشد.', 'danger')
            getcart.save()
        else:
            if is_auth:
                Cart.objects.create(product_id=pid, user_id=request.user.id, variant_id=var_id, quantity=quan, sessionkey=None)
            else:
                Cart.objects.create(user=None, product_id=pid, variant_id=var_id, quantity=quan, sessionkey=session_key)
            messages.success(request, 'تعداد {} تا از این محصول با موفقیت به سبد خرید اضافه شد'.format(quan), 'success')
    return redirect(url)
    # return JsonResponse({'quantity': quan})


def add_cart_single(request):
    print("##################################################333")
    quan = request.GET.get('quantity')
    variant_id = request.GET.get('variant_id')
    product = Product.objects.get(id=request.GET.get('product_id'))
    is_auth = request.user.is_authenticated
    session_key = request.session.session_key
    user_id = request.user.id

    if product.status != 'None':
        cart = Cart.objects.filter(user_id=user_id if is_auth else None, variant_id=variant_id, sessionkey=session_key if not is_auth else None)
        flag = True if cart.exists() else False
    else:
        cart = Cart.objects.filter(user_id=user_id if is_auth else None, product_id=pid, sessionkey=session_key if not is_auth else None)
        flag = True if cart.exists() else False

    if flag:
        if product.status != 'None':
            getcart = Cart.objects.get(user_id=user_id if is_auth else None, product_id=pid, variant_id=variant_id, sessionkey=session_key if not is_auth else None)
            if getcart.variant.amount >= getcart.quantity + quan > 0:
                getcart.quantity += quan
            elif getcart.quantity + quan > getcart.variant.amount:
                messages.error(request, 'درخواست بیش از حد موجودی است.', 'danger')
            elif getcart.quantity + quan <= 0:
                messages.error(request, 'تعداد محصول نمیتواند کمتر از 1 باشد.', 'danger')
        else:
            getcart = Cart.objects.get(user_id=user_id if is_auth else None, product_id=pid,
                                       sessionkey=session_key if not is_auth else None)
            if getcart.product.amount >= getcart.quantity + quan > 0:
                getcart.quantity += quan
            elif getcart.quantity + quan > getcart.product.amount:
                messages.error(request, 'درخواست بیش از حد موجودی است.', 'danger')
            elif getcart.product + quan <= 0:
                messages.error(request, 'تعداد محصول نمیتواند کمتر از 1 باشد.', 'danger')
        getcart.save()
    else:
        if is_auth:
            Cart.objects.create(product_id=pid, user_id=request.user.id, variant_id=variant_id, quantity=quan,
                                sessionkey=None)
        else:
            Cart.objects.create(user=None, product_id=pid, variant_id=variant_id, quantity=quan, sessionkey=session_key)
        messages.success(request, 'تعداد {} تا از این محصول با موفقیت به سبد خرید اضافه شد'.format(quan), 'success')
    return JsonResponse({'success': 'done'})


def remove_cart(request, cid):
    url = request.META.get('HTTP_REFERER')
    Cart.objects.filter(id=cid).delete()
    return redirect(url)


def compare(request, pid):
    url = request.META.get('HTTP_REFERER')
    item = get_object_or_404(Product.objects.filter(id=pid))
    if request.user.is_authenticated:
        qs = Compare.objects.filter(user_id=request.user.id, product_id=pid)
        if qs.exists():
            messages.success(request, 'قبلا به سبد مقایسه اضافه شده')
        else:
            Compare.objects.create(user_id=request.user.id, product_id=pid, sessionkey=None)
    else:
        qs = Compare.objects.filter(user_id=None, product_id=pid, sessionkey=request.session.session_key)
        if qs.exists():
            messages.success(request, 'قبلا به سبد مقایسه اضافه شده2')
        else:
            if not request.session.session_key:
                request.session.create()
            Compare.objects.create(user_id=request.user.id, product=pid, sessionkey=request.session.session_key)
    return redirect(url)


def show_compare(request):
    if request.user.is_authenticated:
        data = Compare.objects.filter(user_id=request.user.id)
        return render(request, 'cart/show-comp.html', {'data': data})
    else:
        data = Compare.objects.filter(sessionkey__exact=request.session.session_key, user_id=None)
        return render(request, 'cart/show-comp.html', {'data': data})
