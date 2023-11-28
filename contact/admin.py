from django.contrib import admin
from .models import contactForm
from .forms import contForm

class ContactUsAdmin(admin.ModelAdmin):
    form = contForm
    list_display = ('full_name', 'email', 'phone_number',
                    'input_text',)


admin.site.register(contactForm, ContactUsAdmin)
