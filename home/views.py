from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Category, Product, Variant, CommentForm, Comment, ReplyForm, Images
from cart.models import Cart, CartForm
from .forms import SearchForm
from django.contrib import messages
from django.db.models import Q, Max, Min
from django.core.mail import EmailMessage
from django.core.paginator import Paginator
from django.template.defaulttags import register
from .filters import ProductFilter
from urllib.parse import urlencode


@register.filter
def get_range(value):
    return range(value)


def mainpage(request):
    categories = Category.objects.filter(is_subcategory=False)
    form = SearchForm()
    return render(request, 'home/home.html', {'categories': categories, 'form': form})


def all_products(request, slug=None):
    category = Category.objects.filter(is_subcategory=False)
    form = SearchForm()
    '''
    if we want to search in this view
    remove method and change action of form
    '''
    # if 'search' in request.GET:
    #     form = SearchForm(request.GET)
    #     if form.is_valid():
    #         data = form.cleaned_data['search']
    #         if data is not None:
    #             products = products.filter(Q(name__contains=data))
    #         if not products.exists():
    #             messages.error(request, 'محصولی با اسم \"{}\" یافت نشد'.format(data), 'danger')
    #     else:
    #         messages.error(request, 'مقدار سرچ نباید خالی باشد', 'danger')
    #     return render(request, 'home/products.html', {'products': products, 'form': form}
    products = Product.objects.all()
    maxprice = int(products.aggregate(unit_price=Max('unit_price'))['unit_price'])
    minprice = int(products.aggregate(unit_price=Min('unit_price'))['unit_price'])
    filtr = ProductFilter(request.GET, queryset=products)
    products = filtr.qs
    perpage = 8
    paginator = Paginator(products, per_page=perpage)
    pageindex = request.GET.get('page')
    pageobjects = paginator.get_page(pageindex)

    if slug:
        data = get_object_or_404(Category, slug=slug)  # get_object_or_404(Category, slug=slug)
        pageobjects = products.filter(category=data)
        paginator = Paginator(pageobjects, per_page=perpage)
        pageindex = request.GET.get('page')
        pageobjects = paginator.get_page(pageindex)
    pagecount = paginator.num_pages
    dataget = request.GET.copy()
    if 'page' in dataget:
        del dataget['page']
    context = {
        'products': pageobjects, 'category': category, 'form': form, 'maxprice': maxprice, 'minprice': minprice,
        'pageindex': pageindex, 'pagecount': range(1, pagecount+1), 'filter': filtr, 'dataget': urlencode(dataget),
    }
    return render(request, 'home/products.html', context=context)


def product_detail(request, slug):
    # product = Product.objects.get(slug=slug)
    product = get_object_or_404(Product, slug=slug)
    images = Images.objects.filter(product__slug=slug)
    comment_form = CommentForm()
    comments = Comment.objects.filter(product__slug=slug, is_reply=False)
    similar = product.tags.similar_objects()[:8]
    cart_form = CartForm()
    is_liked = False
    if product.like.filter(id=request.user.id).exists():
        is_liked = True
    is_favourite = False
    if product.favourite_users.filter(id=request.user.id).exists():
        is_favourite = True
    if product.status is not None:
        variants = Variant.objects.filter(product__slug=slug)
        if request.method == 'POST':
            varid = request.POST.get('select')
            variant = Variant.objects.get(id=varid)
        elif request.method == 'GET':
            variant = Variant.objects.get(id=variants[0].id)
        context = {
            'product': product, 'variant': variant, 'variants': variants, 'similar': similar, 'cart_form': cart_form,
            'is_liked': is_liked, 'is_favourite': is_favourite, 'comment_form': comment_form, 'comments': comments,
        }
        return render(request, 'home/detail.html', context=context)
    else:
        return render(request, 'home/detail.html', {
            'product': product, 'similar': similar, 'comment_form': comment_form, 'is_favourite': is_favourite,
            'comments': comments, 'cart_form': cart_form, 'is_liked': is_liked,
        })


def like_product(request, pid):
    url = request.META.get('HTTP_REFERER')
    product = get_object_or_404(Product, id=pid)
    if request.user.is_authenticated:
        if product.like.filter(id=request.user.id).exists():
            product.like.remove(request.user)
        else:
            product.like.add(request.user)
    else:
        messages.success(request, 'برای لایک محصول ابتدا باید وارد شوید', 'danger')
    return redirect(url)


def product_comment(request, pid):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST' and request.user.is_authenticated:
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            data = comment_form.cleaned_data
            Comment.objects.create(user_id=request.user.id, comment=data['comment'], rate=data['rate'], product_id=pid)
    else:
        messages.success(request, 'برای کامنت گذاشتن ابتدا باید وارد شوید', 'danger')
    return redirect(url)


def comment_reply(request, pid, comment_id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST' and request.user.is_authenticated:
        reply_form = ReplyForm(request.POST)
        if reply_form.is_valid():
            data = reply_form.cleaned_data
            Comment.objects.create(comment=data['comment'], product_id=pid, user_id=request.user.id,
                                   reply_id=comment_id, is_reply=True)
            messages.success(request, 'thanks for reply', 'primary')
    else:
        messages.success(request, 'برای کامنت گذاشتن ابتدا باید وارد شوید', 'danger')
    return redirect(url)


def comment_like(request, cid):
    url = request.META.get('HTTP_REFERER')
    comment = Comment.objects.get(id=cid)
    if request.user.is_authenticated:
        if comment.like.filter(id=request.user.id).exists():
            comment.like.remove(request.user)
        else:
            comment.like.add(request.user)
            messages.success(request, 'ممنون از لابک کامنت', 'success')
    else:
        messages.success(request, 'برای لایک کامنت ابتدا باید وارد شوید', 'danger')
    return redirect(url)


def product_search(request):
    products = Product.objects.all()
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data['search']
            if data is not None:
                products = products.filter(Q(name__contains=data))
            if not products.exists():
                messages.error(request, 'محصولی با اسم \"{}\" یافت نشد'.format(data), 'danger')
        else:
            messages.error(request, 'مقدار سرچ نباید خالی باشد', 'danger')
        return render(request, 'home/products.html', {'products': products, 'form': form})
    else:
        messages.error(request, 'دست نکن یچه :)', 'danger')
        return render(request, 'home/products.html', {'products': products})


def add_favourite(request, pid):
    url = request.META.get('HTTP_REFERER')
    product = Product.objects.get(id=pid)
    if product.favourite_users.filter(id=request.user.id).exists():
        product.favourite_users.remove(request.user)
        product.favcount -= 1
        product.save()
    else:
        product.favourite_users.add(request.user)
        product.favcount += 1
        product.save()
    return redirect(url)


def contact(request):
    if request.method == 'POST':
        subject, email = request.POST['subject'], request.POST['email']
        msg = request.POST['message']
        emailform = EmailMessage(
            'contact form', f'{subject}\n{email}\n\t{msg}', 'dev-shop.ir<reply>', ('soroush8fathi@gmail.com', )
        )
        emailform.send(fail_silently=False)
    return render(request, 'home/contact.html')
