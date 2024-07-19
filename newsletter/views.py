from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Subscriber
from .forms import SubscriberForm, UnsubscribeForm


def add_subscriber(request):
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            existing_subscriber = Subscriber.objects.filter(email=instance.email).first()
            if existing_subscriber:
                if existing_subscriber.is_subscribed:
                    messages.error(request, f"{existing_subscriber.email} already exists in our database.")
                else:
                    existing_subscriber.is_subscribed = True
                    existing_subscriber.save()
                    messages.success(request, f"{existing_subscriber.email} has been re-subscribed to the newsletter")
            else:
                instance.save()
                messages.success(request, f"{instance.email} has been added to our newsletter")
        else:
            messages.error(request, "Please correct the error below.")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def unsubscribe(request):
    if request.method == 'POST':
        form = UnsubscribeForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            try:
                subscriber = Subscriber.objects.get(email=email)
                if not subscriber.is_subscribed:
                    messages.error(request, f"{email} is already unsubscribed.")
                else:
                    subscriber.unsubscribe()
                    messages.success(request, f"Successfully unsubscribed {email} from our newsletter.")
            except Subscriber.DoesNotExist:
                messages.error(request, f"No subscriber found with the email {email}.")
        else:
            messages.error(request, "Invalid form submission.")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
