from django.db.models import Q
from django.views.generic import DetailView, ListView

from mygadget.models import CartItem, Product


class ProductListView(ListView):
    model = Product
    template_name = "product_list.html"
    context_object_name = "products"

    def get_queryset(self):
        return Product.objects.all()


class ProductDetailView(DetailView):
    model = Product
    template_name = "product_detail.html"
    context_object_name = "product"

    def get_queryset(self):
        return Product.objects.all()


class CartItemView(ListView):
    model = CartItem
    template_name = "cart_item_list.html"
    context_object_name = "cart_items"

    def get_queryset(self):
        cart_items = CartItem.objects.filter(customer=self.request.user, is_active=True)
        params = self.request.GET
        search_fields = ["product__name", "product__description"]

        for param_name, param_value in params.items():
            if param_name == "search":
                or_filter = Q()
                for field in search_fields:
                    or_filter |= Q(**{f"{field}__icontains": param_value})
                cart_items = cart_items.filter(or_filter)
            else:
                cart_items = cart_items.filter(**{param_name: param_value})

        return cart_items
