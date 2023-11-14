from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver


class UserProfile(models.Model):
    """
    A user profile model for maintaining default
    information and order history
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_full_name = models.CharField(max_length=50, null=True, blank=True)
    default_phone_number = models.CharField(max_length=20, null=True, blank=True)
    default_email = models.EmailField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.user.username