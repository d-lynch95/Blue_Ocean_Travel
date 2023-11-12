from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Product, Region
from django.contrib import messages
from django.db.models import Q

def view_products(request):
    """ A view to show individual product details """

    products = Product.objects.all()
    query = None
    location = None

    if request.GET:
        if 'region' in request.GET:
            location = request.GET['region'].split(',')
            products = products.filter(region__name__in=location)
            location = Region.objects.filter(name__in=location)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
        'current_region': location,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show all products, including sorting and search queries """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)