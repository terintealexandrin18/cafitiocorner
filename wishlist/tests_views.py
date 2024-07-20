from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from profiles.models import UserProfile
from products.models import Product
from wishlist.models import Wishlist


class WishlistViewTests(TestCase):
    """
    Test cases for the Wishlist views.
    """

    def setUp(self):
        """
        Set up the test environment with a user, user profile, and products.
        """
        self.user = User.objects.create_user(
            username='testuser', password='testpass')
        self.user_profile = UserProfile.objects.get(user=self.user)
        self.product1 = Product.objects.create(name='Product 1', price=10.00)
        self.product2 = Product.objects.create(name='Product 2', price=20.00)
        self.client.login(username='testuser', password='testpass')

    def test_wishlist_view(self):
        """
        Test the wishlist view returns the correct status code and template.
        """
        response = self.client.get(reverse('wishlist'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'wishlist/wishlist.html')

    def test_toggle_wishlist_add(self):
        """
        Test adding a product to the wishlist.
        """
        response = self.client.get(
            reverse('toggle_wishlist', args=[self.product1.id]))
        self.assertRedirects(response, reverse('products'))
        self.assertTrue(
            Wishlist.objects.filter(
                user_profile=self.user_profile,
                product=self.product1
            ).exists()
        )

    def test_toggle_wishlist_remove(self):
        """
        Test removing a product from the wishlist.
        """
        Wishlist.objects.create(
            user_profile=self.user_profile, product=self.product1)
        response = self.client.get(
            reverse('toggle_wishlist', args=[self.product1.id]))
        self.assertRedirects(response, reverse('products'))
        self.assertFalse(
            Wishlist.objects.filter(
                user_profile=self.user_profile,
                product=self.product1
            ).exists()
        )
