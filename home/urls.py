from django.urls import path, re_path
from . import views
app_name = 'home'  # namespace in proj/urls.py
urlpatterns = [
    path('', views.mainpage, name='mainpage'),  # name for use in template
    path('products/', views.all_products, name='products'),
    # todo: use re_path and regex for slug
    path('category/<slug>/', views.all_products, name='category'),
    path('detail/<slug>/', views.product_detail, name='detail'),
    path('like/<int:pid>/', views.like_product, name='like'),
    path('comment/<int:pid>/', views.product_comment, name='comment')
]
