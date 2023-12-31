from django.forms.widgets import ClearableFileInput
from django.utils.translation import gettext_lazy as _


class CustomClearableFileInput(ClearableFileInput):
    initial_text = _('Current Image')
    input_text = _('')
    template_name = 'staff/custom_widgets_templates/custom_clearable_file_input.html'