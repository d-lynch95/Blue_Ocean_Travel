from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.
from products.models import Product


class WishlistItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True)
