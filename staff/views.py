from django.views import generic
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from products.models import Product
from contact.models import contactForm
from contact.forms import contForm
from .forms import ProductForm

from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse


def staff_view(request):
    """ A view for staff to access a page only they can see """
    contact_forms = contactForm.objects.all()
    return render(request,
                  'staff/staff.html',
                  {'contact_forms': contact_forms})


# Allow staff members to add new tours to the store
@login_required
def add_product(request):
    """ Add a tour to the store """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request,
                           'Failed to add product. \
                           Please ensure the form is valid.')
    else:
        form = ProductForm()
    template = 'staff/add_tour.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


# Allow staff members to edit existing tours
@login_required
def edit_product(request, product_id):
    """ Edit a tour in the store """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product.\
                            Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'staff/edit_tour.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


# Allows staff to delete tours from the site
def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        product.delete()
        messages.success(request, 'Product has been deleted')
        return redirect('/products/')
    return render(request, 'staff/delete_tour.html', {'product': product})
