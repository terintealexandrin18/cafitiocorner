from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from products.models import Product, Review
from profiles.models import UserProfile


class ReviewViewsTests(TestCase):
    """
    Test cases for the review-related views.
    """

    def setUp(self):
        """
        Set up the test client and initial data for the tests.
        """
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        self.user_profile, created = UserProfile.objects.get_or_create(
            user=self.user)
        self.product = Product.objects.create(
            name='Test Product',
            description='Test Description',
            price=9.99
        )
        self.submit_review_url = reverse(
            'submit_review', args=[self.product.id])
        self.edit_review_url = lambda review_id: reverse(
            'edit_review', args=[review_id])
        self.delete_review_url = lambda review_id: reverse(
            'delete_review', args=[review_id])

    def test_submit_review(self):
        """
        Test submitting a review for a product.
        """
        response = self.client.post(self.submit_review_url, {
            'rating': 5,
            'comment': 'Great product!'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse(
            'product_detail', args=[self.product.id]))
        review = Review.objects.get(product=self.product, user=self.user)
        self.assertEqual(review.rating, 5)
        self.assertEqual(review.comment, 'Great product!')

    def test_edit_review(self):
        """
        Test editing an existing review.
        """
        review = Review.objects.create(
            product=self.product,
            user=self.user,
            rating=4,
            comment='Good product.'
        )

        response = self.client.post(self.edit_review_url(review.id), {
            'rating': 3,
            'comment': 'Average product.'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse(
            'product_detail', args=[self.product.id]))
        review.refresh_from_db()
        self.assertEqual(review.rating, 3)
        self.assertEqual(review.comment, 'Average product.')

    def test_delete_review(self):
        """
        Test deleting an existing review.
        """
        review = Review.objects.create(
            product=self.product,
            user=self.user,
            rating=4,
            comment='Good product.'
        )
        response = self.client.post(self.delete_review_url(review.id))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse(
            'product_detail', args=[self.product.id]))
        self.assertFalse(Review.objects.filter(id=review.id).exists())
