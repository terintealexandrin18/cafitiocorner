from django.contrib import admin
from .models import Subscriber

class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_subscribed', 'date_added')
    ordering = ('-date_added',)

admin.site.register(Subscriber, SubscriberAdmin)