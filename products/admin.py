from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Product, Category, Review


class ProductAdmin(SummernoteModelAdmin):
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
    list_display = ('friendly_name', 'name', 'parent')
    list_filter = ('parent',)

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.select_related('parent')
        return queryset

    def parent(self, obj):
        return obj.parent.friendly_name if obj.parent else None
    parent.admin_order_field = 'parent__friendly_name'
    parent.short_description = 'Parent Category'


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('product', 'user', 'rating', 'comment', 'created_at')
    list_filter = ('rating', 'created_at')
    search_fields = ('product__name', 'user__username', 'comment')


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Review, ReviewAdmin)
