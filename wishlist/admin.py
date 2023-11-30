from django.contrib import admin

from wishlist.models import WishlistItem


class WishlistItemAdmin(admin.ModelAdmin):

    list_display = (
        "user",
        "product",
    )

admin.site.register(WishlistItem, WishlistItemAdmin)