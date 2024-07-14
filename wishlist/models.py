from django.db import models
from profiles.models import UserProfile 
from products.models import Product

class Wishlist(models.Model):
    """
    A Wishlist model for users to keep track of their favorite products.
    """
    user_profile = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name='user_wishlist'
    )
    product = models.ForeignKey(
        Product,
        null=False,
        blank=False,
        related_name='wishlists',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.product.name} in wishlist of {self.user_profile.user.username}"
