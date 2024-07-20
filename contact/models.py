from django.db import models


class ContactMessage(models.Model):
    """
    Model to represent a contact message submitted by a user.
    """
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        String representation of the ContactMessage model.
        """
        return f'{self.name} - {self.subject}'
