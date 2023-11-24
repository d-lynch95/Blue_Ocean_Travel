from django.contrib import admin
from .models import contact_us

class ContactUsAdmin(admin.ModelAdmin):

    verbose_name_plural = 'Contact Forms'

    readonly_fields = ( 'full_name', 'email','phone_number',
                        'input_text','selection',)

    fields = ('full_name', 'email','phone_number',
                'input_text','selection',)

    list_display = ('full_name', 'email', 'phone_number',
                    'input_text','selection',)

admin.site.register(contact_us, ContactUsAdmin)

