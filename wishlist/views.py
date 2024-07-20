from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from profiles.models import UserProfile
from products.models import Product
from .models import Wishlist


@login_required
def wishlist(request):
    """
    Display the user's wishlist.
    """
    user_profile = UserProfile.objects.get(user=request.user)
    user_wishlist = Wishlist.objects.filter(
        user_profile=user_profile).order_by('id')
    context = {'user_wishlist': user_wishlist}
    return render(request, 'wishlist/wishlist.html', context)


@login_required
def toggle_wishlist(request, product_id):
    """
    Add or remove a product from the user's wishlist.
    """
    product = get_object_or_404(Product, pk=product_id)
    user_profile = UserProfile.objects.get(user=request.user)
    wishlist_item, created = Wishlist.objects.get_or_create(
        user_profile=user_profile, product=product)
    if not created:
        wishlist_item.delete()
        messages.success(request, f'{product.name} removed from '
                         'Wishlist successfully!')
    else:
        messages.success(request, f'{product.name} added to '
                         'Wishlist successfully!')
    return redirect(request.META.get('HTTP_REFERER', 'products'))
