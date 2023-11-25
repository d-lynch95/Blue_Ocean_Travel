from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views import generic
from django.views.generic import ListView, UpdateView, CreateView, DeleteView

from .forms import ContactSubmit
from .models import contactForm

def contact(request):
    return render(request, 'contact/contact.html')

class ContactList(generic.ListView):
    model = contactForm
    queryset = contactForm.objects.order_by('id')
    template_name = 'contact_form_submissions.html'

    # Only Staff can see the contact requests
    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return contactForm.objects.order_by('date')
        else:
            return redirect('contact.html')

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