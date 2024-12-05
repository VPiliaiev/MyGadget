from django.contrib import admin

from mygadget.models import (CartItem, Comparison, Order, Product,
                             ProductCategory, ProductImage, Wishlist)


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ("customer", "product", "quantity", "is_active")
    search_fields = ("customer__first_name", "customer__last_name", "product__name")
    list_filter = ("is_active", "customer")


@admin.register(Comparison)
class ComparisonAdmin(admin.ModelAdmin):
    list_display = ("customer", "created_at")
    search_fields = ("customer__first_name", "customer__last_name")
    filter_horizontal = ("products",)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("customer", "order_date", "total_amount", "is_active")
    search_fields = ("customer__first_name", "customer__last_name", "products__name")
    list_filter = ("is_active", "order_date")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "price", "stock")
    search_fields = ("name", "category__name")
    list_filter = ("category", "price")


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    search_fields = ("name",)


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ("product", "image", "alt_text")


@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ("customer", "product", "added_at")
    search_fields = ("customer__first_name", "customer__last_name", "product__name")
