from django.db import models
from djmoney.models.fields import MoneyField

from accounts.models import BaseModel, Customer


class CartItem(BaseModel):
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name="cart_items"
    )
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Cart item: {self.product.name} for {self.customer.get_full_name()}"


class Comparison(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name="comparisons"
    )
    products = models.ManyToManyField("Product", related_name="comparisons")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comparison for {self.customer.get_full_name()}"


class Order(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name="orders"
    )
    products = models.ManyToManyField("Product", related_name="orders")
    order_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Order {self.id} by {self.customer.get_full_name()}"


class ProductCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        related_name="subcategories",
        blank=True,
        null=True,
    )

    def get_breadcrumbs(self):
        breadcrumbs = []
        category = self
        while category:
            breadcrumbs.insert(0, category)
            category = category.parent
        return breadcrumbs

    @classmethod
    def create_default_categories(cls):
        default_categories = [
            {
                "name": "Smartphones",
                "description": "Smartphones from various brands",
                "parent": None,
            },
            {
                "name": "Tablets",
                "description": "Tablets for work and entertainment",
                "parent": None,
            },
            {
                "name": "Laptops",
                "description": "Laptops for home and office use",
                "parent": None,
            },
            {
                "name": "Headphones",
                "description": "Headphones for music and gaming",
                "parent": None,
            },
            {
                "name": "Watches",
                "description": "Smartwatches and classic models",
                "parent": None,
            },
            {
                "name": "Apple",
                "description": "Apple smartphones",
                "parent": "Smartphones",
            },
            {
                "name": "Samsung",
                "description": "Samsung smartphones",
                "parent": "Smartphones",
            },
        ]
        categories = {}
        for category_data in default_categories:
            parent_name = category_data.pop("parent", None)
            parent = categories.get(parent_name)
            category_data["parent"] = parent
            category, _ = cls.objects.get_or_create(
                name=category_data["name"], defaults=category_data
            )
            categories[category.name] = category

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = MoneyField(max_digits=14, decimal_places=2, default_currency="UAH")
    stock = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(
        ProductCategory, on_delete=models.SET_NULL, null=True, related_name="products"
    )

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="images"
    )
    image = models.ImageField(upload_to="product_images/")
    alt_text = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Image for {self.product.name}"


class Wishlist(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name="wishlists"
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product} in wishlist of {self.customer.get_full_name()}"
