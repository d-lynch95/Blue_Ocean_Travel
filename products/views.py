from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Product, Region, Review
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

def view_products(request):
    """ A view to show individual product details """

    products = Product.objects.all()
    query = None
    location = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

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


    current_sorting = f'{sort}_{direction}'
    
    context = {
        'products': products,
        'search_term': query,
        'current_region': location,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show all products, including sorting and search queries """

    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        rating = request.POST.get('rating', 5)
        content = request.POST.get('content','')

        if content:
            reviews = Review.objects.filter(created_by=request.user, product=product)
            
            if reviews.count() > 0:
                review=reviews.first()
                review.rating = rating
                review.content = content
                review.save()
            else:
                review = Review.objects.create(
                    product=product,
                    rating=rating,
                    content=content,
                    created_by=request.user
                )
            messages.success(request, f'Your review has been submitted')

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)

