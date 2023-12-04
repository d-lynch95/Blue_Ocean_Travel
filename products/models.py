from django.db import models
from django.contrib.auth.models import User


# Model to segment products by different locations
class Region(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


# Model to view different products
class Product(models.Model):
    region = models.ForeignKey('Region', null=True,
                               blank=True, on_delete=models.SET)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    date = models.DateTimeField()
    duration = models.DurationField(null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    def get_rating(self):
        reviews_total = 0

        for review in self.reviews.all():
            reviews_total += review.rating

        if reviews_total > 0:
            return round(reviews_total / self.reviews.count())


# Model to allow users to leave reviews for products

class Review(models.Model):
    product = models.ForeignKey(Product, related_name='reviews',
                                on_delete=models.CASCADE)
    rating = models.IntegerField(default=3)
    content = models.TextField()
    created_by = models.ForeignKey(User, related_name='reviews',
                                   on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
