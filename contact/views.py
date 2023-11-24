from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import ContactSubmit

def contact_us(request):
    contact_form = ContactSubmit()
    template = 'contact/contact.html'
    context = {
        'contact_form': contact_form,
    }
    return render(request, template, context)


def contact_success(request,):
    """
    Handle successful contact us form submissions
    """
    if request.method == 'POST':
        contact_form = ContactSubmit(request.POST)
        if contact_form.is_valid():
            contact_form.save()  # Save the form data to the backend database
            messages.success(
                self.request,
                f'Your form has been submitted.')
            return redirect('/success/')  # Redirect to the success page
    else:
        contact_form = ContactSubmit()
        messages.warning(request, f'Your form was not submitted.')

    context = {
        'contact_form': contact_form,
    } 

    return render(request, 'contact/contact_success.html', context)