from django.contrib import admin

from wishlist.models import Wishlist


@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ("customer", "product", "added_at")
    list_filter = ("customer", "added_at")
    search_fields = ("customer__first_name", "customer__last_name", "product__name")
    date_hierarchy = "added_at"
