from crispy_forms.helper import FormHelper
from django import forms
from .models import Subscriber

class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ('email',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.fields['email'].label = False
        self.fields['email'].widget.attrs.update({
            'placeholder': 'Enter your email',
            'class': 'form-control',
            'required': True,
            'autocomplete': 'email'
        })

class UnsubscribeForm(forms.Form):
    email = forms.EmailField(
        label='Email address',
        widget=forms.EmailInput(attrs={
            'placeholder': 'Email address',
            'class': 'form-control',
            'required': True,
            'autocomplete': 'email'
        })
    )