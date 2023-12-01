from django.views.generic import ListView, View
from django.views.generic.edit import DeleteView
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

from wishlist.models import WishlistItem
from products.models import Product

class WishList(LoginRequiredMixin,  ListView):
    """
    A view that provides the wishlist of products
    """

    template_name = "wishlist/wishlist.html"
    model = WishlistItem

def add_to_wishlist(request, item_id):
    product = Product.objects.get(pk=item_id)
    wishlist, created = WishlistItem.objects.get_or_create(user=request.user, product=product)

    if created:
        messages.success(request, f'Added {product.name} to your wishlist')
    else:
        messages.success(request, f'{product.name} is already on your wishlist')

    return redirect('wishlist')
