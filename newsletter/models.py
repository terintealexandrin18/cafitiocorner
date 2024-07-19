from django.db import models


class Subscriber(models.Model):
    email = models.EmailField()
    date_added = models.DateTimeField(auto_now_add=True)
    is_subscribed = models.BooleanField(default=True)

    def __str__(self):
        return str(self.email)

    def unsubscribe(self):
        self.is_subscribed = False
        self.save()
