from django.test import TestCase
from django.urls import reverse
from django.contrib.messages import get_messages
from .forms import ContactForm
from .models import ContactMessage


class ContactViewTests(TestCase):
    """
    Test cases for the contact_view.
    """

    def test_contact_view_get(self):
        """
        Test GET request to contact_view.
        """
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact/contact.html')
        self.assertIsInstance(response.context['form'], ContactForm)

    def test_contact_view_post_valid(self):
        """
        Test POST request with valid data to contact_view.
        """
        form_data = {
            'name': 'John Doe',
            'email': 'johndoe@example.com',
            'subject': 'Test Subject',
            'message': 'Test message content.'
        }
        response = self.client.post(reverse('contact'), data=form_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('contact'))
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(
            messages[0]), 'Thank you for your message. '
            'We will get back to you soon.')
        self.assertTrue(ContactMessage.objects.filter(
            email='johndoe@example.com').exists())

    def test_contact_view_post_invalid(self):
        """
        Test POST request with invalid data to contact_view.
        """
        form_data = {
            'name': '',
            'email': 'not-an-email',
            'subject': '',
            'message': ''
        }
        response = self.client.post(reverse('contact'), data=form_data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact/contact.html')
        self.assertIsInstance(response.context['form'], ContactForm)
        self.assertFalse(response.context['form'].is_valid())
        self.assertFalse(ContactMessage.objects.exists())
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 0)
