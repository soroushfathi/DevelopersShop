from django.urls import path, re_path
from .views import mainpage, all_products, product_detail, like_product

app_name = 'home'  # namespace in proj/urls.py
urlpatterns = [
    path('', mainpage, name='mainpage'),  # name for use in template
    path('products/', all_products, name='products'),
    # todo: use re_path and regex for slug
    path('category/<slug>/', all_products, name='category'),
    path('detail/<slug>/', product_detail, name='detail'),
    path('like/<int:pid>/', like_product, name='like')
]
