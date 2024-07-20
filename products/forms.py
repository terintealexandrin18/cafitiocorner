from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category, Review


class ProductForm(forms.ModelForm):
    """
    Form class to handle the creation and editing of Product instances.
    Utilizes CustomClearableFileInput for the image field.
    """
    class Meta:
        model = Product
        fields = '__all__'
        exclude = ['rating']
    image = forms.ImageField(label='Image', required=False,
                             widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        """
        Initialize the ProductForm with dynamic category
        choices and custom styles.
        """
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]
        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class ReviewForm(forms.ModelForm):
    """
    Form class to handle the creation and editing of Review instances.
    Includes validation to ensure either rating or comment is provided.
    """
    class Meta:
        model = Review
        fields = ['rating', 'comment']
        widgets = {
            'comment': forms.Textarea(attrs={'rows': 4}),
        }

    def clean(self):
        """
        Custom validation to ensure that at least one of rating or
        comment is provided.
        """
        cleaned_data = super().clean()
        rating = cleaned_data.get('rating')
        comment = cleaned_data.get('comment')
        if not rating and not comment:
            raise forms.ValidationError("At least one of the fields "
                  "(rating or comment) must be filled.")
        return cleaned_data
