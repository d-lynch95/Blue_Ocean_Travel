from django import forms
from .models import contactForm

class contForm(forms.ModelForm):
    class Meta:
        model = contactForm
        fields = ('full_name', 'email', 'phone_number',
                  'input_text', 
                  )

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'input_text': 'How can we help you today?',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True