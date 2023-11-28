from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views import generic, View
from django.views.generic import ListView, UpdateView, CreateView, DeleteView

from .forms import contForm
from .models import contactForm

def contact(request):
    template = "contact/contact.html"
    context = {"contForm": contForm}
    return render(request, template, context)
