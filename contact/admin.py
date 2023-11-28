from django.contrib import admin
from .models import contactForm
from .forms import contForm

class ContactUsAdmin(admin.ModelAdmin):
    form = contForm

    readonly_fields = ( 'full_name', 'email','phone_number',
                        'input_text','selection',)

    fields = ('full_name', 'email','phone_number',
                'input_text','selection',)

    list_display = ('full_name', 'email', 'phone_number',
                    'input_text','selection',)


admin.site.register(contactForm, ContactUsAdmin)
