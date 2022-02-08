from django.urls import path
from .views import mainpage

app_name = 'home'  # namespace in proj/urls.py
urlpatterns = [
    path('', mainpage, name='mainpage'),  # name for use in template
    # path('products',),
]
