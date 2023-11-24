from django.db import models

DESTINATIONS = (
       ('option1', 'Great Barrier Reef'),
       ('option2', 'Whitsundays'),
       ('option3', 'Kgari (Fraser Island)'),
    )

class contactForm(models.Model):
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    input_text = models.TextField(max_length=1000, null=True, blank=True)
    selection = models.IntegerField(choices=DESTINATIONS, default=1)
 