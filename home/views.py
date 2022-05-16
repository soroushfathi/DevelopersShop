from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Category, Product, Variant, CommentForm, Comment
from django.contrib import messages


def mainpage(request):
    categories = Category.objects.filter(is_subcategory=False)
    return render(request, 'home/home.html', {'categories': categories})


def all_products(request, slug=None):
    category = Category.objects.filter(is_subcategory=False)
    products = Product.objects.all()
    if slug:
        # data = Category.objects.get(slug=slug)
        data = get_object_or_404(Category, slug=slug)
        products = products.filter(category=data)
    context = {
        'products': products,
        'category': category,
    }
    return render(request, 'home/products.html', context=context)


def product_detail(request, slug):
    # product = Product.objects.get(slug=slug)
    product = get_object_or_404(Product, slug=slug)
    comment_form = CommentForm()
    comments = Comment.objects.filter(product__slug=slug, is_reply=False)
    similar = product.tags.similar_objects()[:8]
    is_liked = False
    if product.like.filter(id=request.user.id).exists():
        is_liked = True
    if product.status is not None:
        variants = Variant.objects.filter(product__slug=slug)
        if request.method == 'POST':
            varid = request.POST.get('select')
            variant = Variant.objects.get(id=varid)
        elif request.method == 'GET':
            variant = Variant.objects.get(id=variants[0].id)
        context = {
            'product': product, 'variant': variant, 'variants': variants, 'similar': similar,
            'is_liked': is_liked, 'comment_form': comment_form, 'comments': comments,
        }
        return render(request, 'home/detail.html', context=context)
    else:
        return render(request, 'home/detail.html', {
            'product': product, 'similar': similar, 'comment_form': comment_form, 'comments': comments,
        })


def like_product(request, pid):
    url = request.META.get('HTTP_REFERER')
    product = get_object_or_404(Product, id=pid)
    if product.like.filter(id=request.user.id).exists():
        product.like.remove(request.user)
    else:
        product.like.add(request.user)
    return redirect(url)


def product_comment(request, pid):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            data = comment_form.cleaned_data
            Comment.objects.create(user_id=request.user.id, comment=data['comment'], rate=data['rate'], product_id=pid)
        return redirect(url)
