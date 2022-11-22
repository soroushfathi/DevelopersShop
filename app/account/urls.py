from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from .views import (
    register, logins, logouts, dashboard, user_update, change_passsword,
)
from . import views
app_name = 'account'
urlpatterns = [
    path('register/', register, name='register'),
    path('login/', logins, name='login'),
    path('logout/', logouts, name='logout'),
    path('dashboard/', dashboard, name='dashboard'),
    path('update/', user_update, name='update'),
    path('change-password/', change_passsword, name='change-password'),
    path('resend-email-activation/', views.resend_email_activation, name='resend-email-activation'),
    path('email-activation/<uidb64>/<token>/', views.EmailRegister.as_view(), name='email-activation'),
    path('reset-password/', views.ResetPassword.as_view(), name='reset-password'),
    path('reset-password/done/', views.DoneResetPassword.as_view(), name='done-reset-password'),
    path('reset-passwoed/confirm/<uidb64>/<token>/', views.ConfirmResetPassword.as_view(), name='confirm-reset-password'),
    path('reset-password/complete/', views.CompleteResetPassword.as_view(), name='complete-reset-password'),
    path('favourite/', views.favourite, name='favourite'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
