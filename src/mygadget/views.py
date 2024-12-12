from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from mygadget.models import CartItem, Product, ProductCategory


class ProductListView(ListView):
    model = Product
    template_name = "product_list.html"
    context_object_name = "products"

    def get_queryset(self):
        products = Product.objects.all()
        params = self.request.GET
        search_fields = ["name", "description", "category__name"]

        for param_name, param_value in params.items():
            if param_name == "search":
                or_filter = Q()
                for field in search_fields:
                    or_filter |= Q(**{f"{field}__icontains": param_value})
                products = products.filter(or_filter)
            else:
                products = products.filter(**{param_name: param_value})

        return products


class ProductDetailView(DetailView):
    model = Product
    template_name = "product_detail.html"
    context_object_name = "product"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = self.object.category
        if category:
            context["breadcrumbs"] = category.get_breadcrumbs()
        return context


class CartItemView(LoginRequiredMixin, ListView):
    model = CartItem
    template_name = "cart_item_list.html"
    context_object_name = "cart_items"

    def get_queryset(self):
        return CartItem.objects.filter(customer=self.request.user, is_active=True)


class AddToCartView(LoginRequiredMixin, CreateView):
    model = CartItem
    fields = []
    success_url = reverse_lazy("mygadget:cart")

    def form_valid(self, form):
        product = get_object_or_404(Product, id=self.kwargs["pk"])
        cart_item, created = CartItem.objects.get_or_create(
            customer=self.request.user, product=product, defaults={"quantity": 1}
        )
        if not created:
            cart_item.quantity += 1
            cart_item.save()
        return redirect(self.success_url)


class UpdateCartItemView(LoginRequiredMixin, UpdateView):
    model = CartItem
    fields = ["quantity"]
    success_url = reverse_lazy("mygadget:cart")

    def get_queryset(self):
        return CartItem.objects.filter(customer=self.request.user)


class DeleteCartItemView(LoginRequiredMixin, DeleteView):
    model = CartItem
    success_url = reverse_lazy("mygadget:cart")

    def get_queryset(self):
        return CartItem.objects.filter(customer=self.request.user)


class CategoryListView(ListView):
    model = ProductCategory
    template_name = "category_list.html"
    context_object_name = "categories"

    def get_queryset(self):
        return ProductCategory.objects.filter(parent=None)


class CategoryDetailView(DetailView):
    model = ProductCategory
    template_name = "category_detail.html"
    context_object_name = "category"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["subcategories"] = self.object.subcategories.all()
        context["products"] = Product.objects.filter(category=self.object)
        return context
