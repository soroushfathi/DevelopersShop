from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Category, Product, Variant, CommentForm, Comment, ReplyForm, Images
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
    images = Images.objects.filter(product__slug=slug)
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
