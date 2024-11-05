from django.db import models

from accounts.models import Customer
from products.models import Product


class Wishlist(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name="wishlists"
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product} in wishlist of {self.customer.get_full_name()}"
