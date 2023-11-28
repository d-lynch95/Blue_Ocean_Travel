from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ( 'order_number', 'date', 
                        'order_total', )

    fields = ( 'order_number', 'user_profile', 'full_name', 'email',
                'phone_number', 'date', 'order_total',
                'original_bag', 'stripe_pid', )

    list_display = ('order_number', 'date', 'full_name',
                    'order_total',)

    ordering = ('-date',)

admin.site.register(Order, OrderAdmin)
