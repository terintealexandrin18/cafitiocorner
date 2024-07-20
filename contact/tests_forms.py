from django.test import TestCase
from .forms import ContactForm
from .models import ContactMessage


class ContactFormTests(TestCase):
    """
    Test cases for the ContactForm.
    """

    def test_contact_form_valid_data(self):
        """
        Test ContactForm with valid data.
        """
        form_data = {
            'name': 'John Doe',
            'email': 'johndoe@example.com',
            'subject': 'Test Subject',
            'message': 'Test message content.'
        }
        form = ContactForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_contact_form_invalid_data(self):
        """
        Test ContactForm with invalid data.
        """
        form_data = {
            'name': '',
            'email': 'not-an-email',
            'subject': '',
            'message': ''
        }
        form = ContactForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors)
        self.assertIn('email', form.errors)
        self.assertIn('subject', form.errors)
        self.assertIn('message', form.errors)

    def test_contact_form_empty_data(self):
        """
        Test ContactForm with no data.
        """
        form = ContactForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 4)

    def test_contact_form_widget_attributes(self):
        """
        Test the widget attributes of ContactForm fields.
        """
        form = ContactForm()
        for field_name, field in form.fields.items():
            self.assertEqual(
                 field.widget.attrs['class'], 'border-black rounded-0')

    def test_contact_form_helper(self):
        """
        Test that ContactForm initializes the crispy form helper.
        """
        form = ContactForm()
        self.assertTrue(hasattr(form, 'helper'))
        self.assertEqual(form.helper.form_method.upper(), 'POST')
