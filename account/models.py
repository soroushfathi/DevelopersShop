from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from phone_field import PhoneField


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = PhoneField(null=True, blank=True)
    address = models.TextField(max_length=400, null=True, blank=True)
    is_email_active = models.BooleanField(default=False)
    is_phone_active = models.BooleanField(default=False)
    prfile_image = models.ImageField(upload_to='profile/', default='profile/profile.jpg', null=True, blank=True)

    def __str__(self):
        return self.user.username


def save_user_profile(sender, **kwargs):
    if kwargs['created']:
        prof = Profile(user=kwargs['instance'])
        prof.save()


post_save.connect(save_user_profile, sender=User)
