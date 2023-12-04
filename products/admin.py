from django.contrib import admin
from .models import Product, Region, Review

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'region',
        'price',
        'date',
        'duration',
    )

    ordering = ('region',)


class RegionAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'rating',
        'content',
        'created_by',
        'created_at',
    )

    ordering = ('product',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Region, RegionAdmin)
admin.site.register(Review, ReviewAdmin)
