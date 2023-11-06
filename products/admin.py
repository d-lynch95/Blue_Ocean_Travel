from django.contrib import admin
from .models import Product, Region

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


admin.site.register(Product, ProductAdmin)
admin.site.register(Region, RegionAdmin)