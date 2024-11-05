from django.contrib import admin

from accounts.models import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = [
        "first_name",
        "last_name",
        "email",
        "is_staff",
        "is_active",
        "date_joined",
        "birth_date",
        "photo",
    ]
    ordering = ["first_name", "last_name", "date_joined", "birth_date"]
    list_display_links = ["email", "first_name", "last_name"]
    search_fields = ["email", "first_name", "last_name"]
    list_filter = ["is_active", "is_staff"]
    date_hierarchy = "date_joined"
    readonly_fields = ["date_joined"]
    fieldsets = [
        (
            "Personal Info",
            {
                "fields": [
                    "email",
                    "first_name",
                    "last_name",
                    "birth_date",
                    "photo",
                ]
            },
        ),
        ("Details", {"fields": ["is_staff", "is_active"]}),
    ]
