from django import forms
from .widgets import CustomClearableFileInput
from products.models import Product, Region


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(label='Image',
                             required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Region.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['region'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
