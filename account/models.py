from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    # user = models.OneToOneField(User, one_delete=models.CASCADE)
    phone = models.IntegerField(max_length=11)
    address = models.TextField(max_length=400)
