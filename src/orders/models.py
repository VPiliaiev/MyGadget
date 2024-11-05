from django.db import models

from accounts.models import Customer


class OrderHistory(models.Model):
    customer = models.OneToOneField(
        Customer, on_delete=models.CASCADE, related_name="order_history"
    )

    def __str__(self):
        return f"Order history for {self.customer.get_full_name()}"


class Order(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name="orders"
    )
    order_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Order {self.id} by {self.customer.get_full_name()}"
