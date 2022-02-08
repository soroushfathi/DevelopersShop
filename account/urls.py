from django.urls import path
from .views import register, logins, logouts, dashboard

app_name = 'account'
urlpatterns = [
    path('register/', register, name='register'),
    path('login/', logins, name='login'),
    path('logout/', logouts, name='logout'),
    path('dashboard/', dashboard, name='dashboard'),
]
