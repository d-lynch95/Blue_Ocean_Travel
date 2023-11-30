from django.views.generic import ListView, View
from django.views.generic.edit import DeleteView
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

from wishlist.models import WishlistItem

class WishList(LoginRequiredMixin,  ListView):
    """
    A view that provides the wishlist of products
    """

    template_name = "wishlist/wishlist.html"
    model = WishlistItem


