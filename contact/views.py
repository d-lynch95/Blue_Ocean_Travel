from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views import generic, View
from django.contrib import messages
from django.views.generic import ListView, UpdateView, CreateView, DeleteView

from .forms import contForm
from .models import contactForm

def contact(request):
    template = "contact/contact.html"
    context = {"contForm": contForm}
    return render(request, template, context)

def submitForm(request):
    """ allow users to submit contact us form """
    form = contForm()
    if request.method == 'POST':
        form = contForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully submitted form!')
            return redirect( 'success')
        else:
            messages.error(request, 'Your form did not submit')
    else:
        form = contForm()
    template = 'contact/contact.html'
    context = {
        'form': form,
    }
    return render(request, template, context)

def success(request):
    """ A view to return the contact success page """
    return render(request, 'contact/contact_success.html')

