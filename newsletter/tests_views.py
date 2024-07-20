from django.test import TestCase, Client
from .models import Subscriber


class NewsletterViewsTests(TestCase):
    """
    Test cases for the newsletter views.
    """

    def setUp(self):
        """
        Set up the test client and initial data for the tests.
        """
        self.client = Client()
        self.add_subscriber_url = '/newsletter/'
        self.unsubscribe_url = '/newsletter/unsubscribe/'
        self.subscriber_email = 'test@example.com'

        # Create a subscriber
        self.subscriber = Subscriber.objects.create(
            email=self.subscriber_email, is_subscribed=True)

    def test_add_subscriber(self):
        """
        Test adding a new subscriber to the newsletter.
        """
        response = self.client.post(
            self.add_subscriber_url,
            {'email': 'new@example.com'}, HTTP_REFERER='/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')
        self.assertTrue(
            Subscriber.objects.filter(email='new@example.com').exists()
        )

    def test_add_existing_subscriber(self):
        """
        Test adding an existing subscriber to the newsletter.
        """
        response = self.client.post(
            self.add_subscriber_url,
            {'email': self.subscriber_email}, HTTP_REFERER='/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')
        subscriber = Subscriber.objects.get(email=self.subscriber_email)
        self.assertTrue(subscriber.is_subscribed)

    def test_unsubscribe_existing_subscriber(self):
        """
        Test unsubscribing an existing subscriber from the newsletter.
        """
        response = self.client.post(
            self.unsubscribe_url,
            {'email': self.subscriber_email}, HTTP_REFERER='/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')
        subscriber = Subscriber.objects.get(email=self.subscriber_email)
        self.assertFalse(subscriber.is_subscribed)

    def test_unsubscribe_non_existent_subscriber(self):
        """
        Test unsubscribing a non-existent subscriber from the newsletter.
        """
        response = self.client.post(
            self.unsubscribe_url,
            {'email': 'non_existent@example.com'}, HTTP_REFERER='/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')
        self.assertFalse(
            Subscriber.objects.filter(
                email='non_existent@example.com').exists()
        )

    def test_invalid_add_subscriber_form(self):
        """
        Test submitting an invalid add subscriber form.
        """
        response = self.client.post(
            self.add_subscriber_url, {'email': ''}, HTTP_REFERER='/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')
        self.assertFalse(
            Subscriber.objects.filter(email='').exists()
        )

    def test_invalid_unsubscribe_form(self):
        """
        Test submitting an invalid unsubscribe form.
        """
        response = self.client.post(
            self.unsubscribe_url, {'email': ''}, HTTP_REFERER='/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')
        self.assertFalse(
            Subscriber.objects.filter(email='').exists()
        )
