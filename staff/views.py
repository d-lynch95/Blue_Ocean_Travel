from django.views import generic
from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin

from contact.models import contactForm

def staff_view(request):
    """ A view for staff to access a page only they can see """
    return render(request, 'staff/staff.html')

class ContactList(generic.ListView):
    model = contactForm
    queryset = contactForm.objects.order_by('id')
    template_name = 'staff/staff.html'

    # Only Staff can see the contact requests
    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return contactForm.objects.order_by('date')
        else:
            return redirect('index.html')