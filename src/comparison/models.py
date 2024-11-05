from django.db import models

from accounts.models import Customer
from products.models import Product


class Comparison(models.Model):
    customer = models.OneToOneField(
        Customer, on_delete=models.CASCADE, related_name="comparison"
    )
    products = models.ManyToManyField(Product, related_name="comparisons")
    created_at = models.DateTimeField(auto_now_add=True)
