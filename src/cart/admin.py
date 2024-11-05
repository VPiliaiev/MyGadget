from django.contrib import admin

from cart.models import Cart, CartItem


class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 1


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ("customer", "created_at", "updated_at")
    search_fields = ("customer__first_name", "customer__last_name")
    inlines = [CartItemInline]
    readonly_fields = ("created_at", "updated_at")


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ("cart", "product", "quantity")
    list_filter = ("cart__customer",)
    search_fields = ("product__name",)
