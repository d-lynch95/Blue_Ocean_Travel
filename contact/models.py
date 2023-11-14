from django.db import models

class contact_us(models.Model):
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    input_text = models.TextField(max_length=1000, null=True, blank=True)
    options = (
        ('option1', 'Great Barrier Reef'),
        ('option2', 'Whitsundays'),
        ('option3', 'K\'gari (Fraser Island)'),
    )
    selection = models.CharField(max_length=20, choices=options, null=True, blank=True)