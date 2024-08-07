from django import forms
from crispy_forms.helper import FormHelper
from .models import ContactMessage


class ContactForm(forms.ModelForm):
    """
    Form for users to submit contact messages.
    """

    class Meta:
        """
        Meta class to specify the model and fields to include in the form.
        """
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'subject': forms.TextInput(attrs={'placeholder': 'Subject'}),
            'message': forms.Textarea(attrs={'placeholder': 'Message'}),
        }

    def __init__(self, *args, **kwargs):
        """
        Initialize the form and add crispy forms helper for form styling.
        """
        super(ContactForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
