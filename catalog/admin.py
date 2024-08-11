from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Product, Category, Contact, Feedback


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fields = ('name', 'price', 'category', 'image', 'photo_product', 'description')
    list_display = ('id', 'name', 'price', 'category', 'photo_product')
    list_filter = ('category',)
    search_fields = ('name', 'description')
    list_display_links = ('name',)
    readonly_fields = ('photo_product',)

    @admin.display(description="Просмотр")
    def photo_product(self, product: Product):
        if product.image:
            return mark_safe(f"<img src='{product.image.url}' width=50>")
        return "Без изображения"

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['country', 'inn', 'address', 'phone', 'email']

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['created_at', 'name', 'phone', 'message', 'is_read']
    list_filter = ['created_at', 'is_read']
