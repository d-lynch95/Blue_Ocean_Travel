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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['wish_items'] = WishlistItem.objects.filter(user=self.request.user)
        return context

def add_to_wishlist(request, item_id):
    """
    A view to add items to the wishlist
    """
    product = Product.objects.get(pk=item_id)
    wishlist, created = WishlistItem.objects.get_or_create(user=request.user, product=product)

    if created:
        messages.success(request, f'Added {product.name} to your wishlist')
    else:
        messages.success(request, f'{product.name} is already on your wishlist')

    return redirect('wishlist')

def remove_from_wishlist(request, item_id):
    """
    A view to remove items from the wishlist
    """
    item = WishlistItem.objects.get(pk=item_id)
    item.delete()
    messages.success(request, 'Item removed from your wishlist')
    return redirect('wishlist')