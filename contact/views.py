from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import ContactForm

def contact_us(request):
    contact_form = ContactForm()
    template = 'contact/contact.html'
    context = {
        'contact_form': contact_form,
    }

    return render(request, template, context)