from django.contrib import admin
from .models import Subscriber


class SubscriberAdmin(admin.ModelAdmin):
    """
    Admin class for managing Subscriber model in the Django admin interface.
    """
    list_display = ('email', 'is_subscribed', 'date_added')
    ordering = ('-date_added',)


admin.site.register(Subscriber, SubscriberAdmin)
