from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Subscriber
from .forms import SubscriberForm, UnsubscribeForm

def add_subscriber(request):
    form = SubscriberForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)

        existing_subscriber = Subscriber.objects.filter(email=instance.email).first()
        if existing_subscriber:
            if existing_subscriber.is_subscribed:
                messages.error(
                    request,
                    f"{existing_subscriber.email} already exists in our database. "
                    "Please check your email and try again."
                )
            else:
                existing_subscriber.is_subscribed = True
                existing_subscriber.save()
                messages.success(
                    request,
                    f"{existing_subscriber.email} has been re-subscribed to the newsletter"
                )
        else:
            instance.save()
            messages.success(
                request,
                f"{instance.email} has been added to our the newsletter"
            )

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def unsubscribe(request):
    if request.method == 'POST':
        form = UnsubscribeForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            try:
                subscriber = Subscriber.objects.get(email=email)
                subscriber.unsubscribe()
                messages.success(
                    request,
                    f"Successfully unsubscribed {email} from our newsletter."
                )
            except Subscriber.DoesNotExist:
                messages.error(
                    request,
                    f"No subscriber found with the email {email}. "
                    f"Please check your email and try again."
                )
        else:
            messages.error(
                request,
                "Invalid form submission. Check your input and try again."
            )

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
