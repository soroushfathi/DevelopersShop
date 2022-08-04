from django.urls import path
from . import views

app_name = 'order'

urlpatterns = [
    path('history/', views.order_detail, name='detail'),
    path('create/', views.create_order, name='create'),
]
