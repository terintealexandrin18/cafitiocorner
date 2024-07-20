from django.db import models


class Subscriber(models.Model):
    """
    Model to represent a newsletter subscriber.
    """
    email = models.EmailField()
    date_added = models.DateTimeField(auto_now_add=True)
    is_subscribed = models.BooleanField(default=True)

    def __str__(self):
        """
        String representation of the Subscriber model.
        Returns the email address of the subscriber.
        """
        return str(self.email)

    def unsubscribe(self):
        """
        Method to mark the subscriber as unsubscribed.
        """
        self.is_subscribed = False
        self.save()
