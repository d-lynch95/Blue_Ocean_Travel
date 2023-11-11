from django.shortcuts import render
from .models import contact_form

def contact(request):
    """ A view to return the Contact us page """
    return render(request, 'contact/contact.html')