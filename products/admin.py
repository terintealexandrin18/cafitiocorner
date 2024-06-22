from django.contrib import admin
from .models import Product, Category, Review

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )
    
    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('product', 'user', 'rating', 'comment', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('product__name', 'user__username', 'comment')

    actions = ['approve_reviews']

    def approve_reviews(self, request, queryset):
        queryset.update(status='approved')

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Review, ReviewAdmin)
