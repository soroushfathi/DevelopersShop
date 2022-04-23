from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from .views import (
    register, logins, logouts, dashboard, user_update, change_passsword,
)
app_name = 'account'
urlpatterns = [
    path('register/', register, name='register'),
    path('login/', logins, name='login'),
    path('logout/', logouts, name='logout'),
    path('dashboard/', dashboard, name='dashboard'),
    path('update/', user_update, name='update'),
    path('change-password/', change_passsword, name='change-password')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
