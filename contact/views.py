from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views import generic
from django.views.generic import ListView, UpdateView, CreateView, DeleteView

from .forms import ContactSubmit
from .models import contactForm

def contact(request):
    template = "contact/contact.html"
    context = {"contactForm": contactForm}
    return render(request, template, context)

class SubmitForm(LoginRequiredMixin, generic.CreateView):
    def get(self, request):
        form = ContactSubmit()
        context = {"contactForm": contactForm}
        return render(request, 'contact.html', context)

    def post(self, request):
        form = contactForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            messages.success(
                self.request,
                f'Your contact form has been sent')
            return redirect("/contact_success/")

        else:
            context = {"contactForm": contactForm}
            return render(request, 'contact.html', context)