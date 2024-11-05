from django.contrib import admin

from orders.models import Order, OrderHistory

admin.site.register([Order, OrderHistory])
