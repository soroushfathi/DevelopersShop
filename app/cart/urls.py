from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'cart'
urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('add-cart/<int:pid>/', views.add_cart, name='add_cart'),
    path('add-cart/', views.add_cart_single, name='add_single_cart'),
    path('remove/<int:cid>/', views.remove_cart, name='remove_cart'),
    path('compare/<int:pid>/', views.compare, name='compare'),
    path('show-compare/', views.show_compare, name='show_compare'),
]
