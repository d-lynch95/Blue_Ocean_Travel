from django.shortcuts import render

class WishList(LoginRequiredMixin, UserPassesTestMixin, ListView):
    """
    A view that provides the wishlist of products
    """

    template_name = "wishlist/wishlist.html"
    model = WishlistLine


