from django.db import models
from django.db.models import Avg
from django.forms import ModelForm
from django.urls import reverse
from ckeditor.fields import RichTextField
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
from django_jalali.db import models as jmodels
from django.db.models.signals import post_save
# from ckeditor_uploader.fields import RichTextUploadingField # for adding images


class Category(models.Model):
    sub_category = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='sub')
    is_subcategory = models.BooleanField(default=False)
    name = models.CharField(max_length=50)
    slug = models.SlugField(allow_unicode=True, unique=True, null=True, blank=True)
    created = jmodels.jDateTimeField(auto_now_add=True)
    update = jmodels.jDateTimeField(auto_now=True)
    image = models.ImageField(upload_to='category', null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home:category', args=[self.slug])

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'


class Product(models.Model):
    VARIANT = (
        ('None', 'none'),
        ('Size', 'size'),
        ('Color', 'color'),
    )
    category = models.ManyToManyField(Category, blank=True)
    name = models.CharField(max_length=100)
    slug = models.SlugField(allow_unicode=True, unique=True, null=True, blank=True)
    available = models.BooleanField(default=True)
    amount = models.PositiveIntegerField()
    unit_price = models.PositiveIntegerField()
    discount = models.PositiveIntegerField(blank=True, null=True)
    total_price = models.PositiveIntegerField()
    information = RichTextField(blank=True, null=True)
    create = jmodels.jDateTimeField(auto_now_add=True)
    update = jmodels.jDateTimeField(auto_now=True)
    status = models.CharField(max_length=30, null=True, blank=True, choices=VARIANT)
    brand = models.ForeignKey('Brand', on_delete=models.CASCADE, blank=True, null=True)
    size = models.ManyToManyField('Size', blank=True)
    color = models.ManyToManyField('Color', blank=True)
    image = models.ImageField(upload_to='products')
    tags = TaggableManager(blank=True)
    like = models.ManyToManyField(User, blank=True, related_name='user_like')
    like_count = models.IntegerField(default=0)
    unlike = models.ManyToManyField(User, blank=True, related_name='user_unlike')
    unlike_count = models.IntegerField(default=0)
    favourite_users = models.ManyToManyField(User, blank=True, related_name='favourits')
    favcount = models.IntegerField(default=0)
    sellcount = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home:detail', args=[self.slug])

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'

    @property
    def total_price(self):
        if not self.discount:
            return self.unit_price
        else:
            return self.unit_price * (100 - self.discount) // 100

    @property
    def like_count(self):
        return self.like.count()

    @property
    def unlike_count(self):
        return self.like.count()

    @property
    def available(self):
        if self.amount:
            return True
        else:
            return False

    def average(self):
        data = Comment.objects.filter(is_reply=False, product=self).aggregate(avg=Avg('rate'))
        '''
        data = { 'rate': ### }
        '''
        star = 0
        if data['avg'] is not None:
            star = round(data['avg'], 1)
        return star


class Color(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'رنگ بندی'
        verbose_name_plural = 'رنگ بندی ها'


class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Size(models.Model):
    name = models.CharField(max_length=50)
    color = models.ForeignKey(Color, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'{self.name}, {self.color}'

    class Meta:
        verbose_name = 'سایز بندی'
        verbose_name_plural = 'سایز بندی ها'


class Variant(models.Model):
    name = models.CharField(max_length=30)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE, blank=True, null=True)
    color = models.ForeignKey(Color, on_delete=models.CASCADE, blank=True, null=True)
    amount = models.PositiveIntegerField()
    unit_price = models.PositiveIntegerField()
    discount = models.PositiveIntegerField(blank=True, null=True)
    total_price = models.PositiveIntegerField()
    update = jmodels.jDateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    @property
    def total_price(self):
        if not self.discount:
            return self.unit_price
        else:
            return self.unit_price * (100 - self.discount) // 100

    class Meta:
        verbose_name = 'گونه'
        verbose_name_plural = 'گونه ها'


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField()
    # todo: like & dislike a comment
    rate = models.PositiveIntegerField(default=0)
    create = jmodels.jDateTimeField(auto_now_add=True)
    reply = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='comment_replied')
    is_reply = models.BooleanField(default=False)
    like = models.ManyToManyField(User, blank=True, related_name='comment_liked')
    like_count = models.PositiveIntegerField(default=0)

    @property
    def like_count(self):
        return self.like.count()

    def __str__(self):
        return '{}, {}'.format(self.user.username, self.product.name)

    class Meta:
        verbose_name = 'نظر'
        verbose_name_plural = 'نظرات'


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['comment', 'rate']


class ReplyForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']


class Images(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=True)
    image = models.ImageField(upload_to='image/', blank=True)

    class Meta:
        verbose_name = 'تصویر'
        verbose_name_plural = 'تصاویر'


class Chart(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    unit_price = models.IntegerField(default=0)
    update = jmodels.jDateTimeField(auto_now=True)
    color = models.CharField(max_length=50, blank=True, null=True)
    size = models.CharField(max_length=50, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='update_product', blank=True, null=True)
    variant = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='update_product', blank=True, null=True)

    def __str__(self):
        return self.name


def product_update(sender, instance, created, *arsg, **kwargs):
    Chart.objects.create(name=instance.name, product=instance,
                         unit_price=instance['unit_price'], update=instance['update'])


post_save.connect(receiver=product_update, sender=Product)
