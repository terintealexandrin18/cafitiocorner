from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Product, Category, Review


class ProductAdmin(SummernoteModelAdmin):
    """
    Admin class to manage the Product model in the admin interface.
    Utilizes Summernote for the description field.
    """
    summernote_fields = ('description',)
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
    """
    Admin class to manage the Category model in the admin interface.
    """
    list_display = ('friendly_name', 'name', 'parent')
    list_filter = ('parent',)

    def get_queryset(self, request):
        """
        Optimize query by using select_related for parent category.
        Overrides the default get_queryset method to improve query efficiency.
        """
        queryset = super().get_queryset(request)
        queryset = queryset.select_related('parent')
        return queryset

    def parent(self, obj):
        """
        Display friendly name of the parent category.
        Returns the friendly name of the parent category if it exists.
        """
        return obj.parent.friendly_name if obj.parent else None
    parent.admin_order_field = 'parent__friendly_name'
    parent.short_description = 'Parent Category'


class ReviewAdmin(admin.ModelAdmin):
    """
    Admin class to manage the Review model in the admin interface.
    """
    list_display = ('product', 'user', 'rating', 'comment', 'created_at')
    list_filter = ('rating', 'created_at')
    search_fields = ('product__name', 'user__username', 'comment')


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Review, ReviewAdmin)
