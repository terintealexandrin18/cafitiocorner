from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Wishlist
from products.models import Product

@login_required
def wishlist(request):
    wishlist_items = Wishlist.objects.filter(user_profile=request.user.userprofile)
    return render(request, 'wishlist/wishlist.html', {'wishlist_items': wishlist_items})

@login_required
def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    wishlist_item, created = Wishlist.objects.get_or_create(user_profile=request.user.userprofile, product=product)
    if created:
        messages.success(request, f"{product.name} has been added to your wishlist.")
    else:
        messages.info(request, f"{product.name} is already in your wishlist.")
    return redirect('wishlist')

@login_required
def remove_from_wishlist(request, wishlist_item_id):
    wishlist_item = get_object_or_404(Wishlist, id=wishlist_item_id)
    if wishlist_item.user_profile == request.user.userprofile:
        wishlist_item.delete()
        messages.success(request, "Item has been removed from your wishlist.")
    else:
        messages.error(request, "You do not have permission to remove this item.")
    return redirect('wishlist')