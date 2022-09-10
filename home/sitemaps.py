from django.contrib.sitemaps import Sitemap
from .models import Product


class ProductViewSitemap(Sitemap):
    changefreq = 'never'
    priority = 1

    def items(self):
        return Product.objects.all().order_by('-id')

    def lastmod(self, obj):
        return obj.create


