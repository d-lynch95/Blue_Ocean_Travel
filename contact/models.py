from django.db import models

class contact_form(models.Model):
    name = models.CharField(max_length=254)