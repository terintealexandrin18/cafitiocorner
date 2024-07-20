from django.urls import path
from . import views

urlpatterns = [
    path('', views.wishlist, name='wishlist'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path(
        'toggle_wishlist/<int:product_id>/',
        views.toggle_wishlist,
        name='toggle_wishlist'
    ),
]
