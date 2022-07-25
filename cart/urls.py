from django.urls import path
from . import views

app_name = 'cart'
urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('add-cart/<int:pid>', views.add_cart, name='add_cart')
]
