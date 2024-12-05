from django.urls import path

from mygadget.views import (AddToCartView, CartItemView, CategoryDetailView,
                            CategoryListView, DeleteCartItemView,
                            ProductDetailView, ProductListView,
                            UpdateCartItemView)

app_name = "mygadget"

urlpatterns = [
    path("products/", ProductListView.as_view(), name="product_list"),
    path("products/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
    path("catalog/", CategoryListView.as_view(), name="category_list"),
    path("category/<int:pk>/", CategoryDetailView.as_view(), name="category_detail"),
    path("cart/", CartItemView.as_view(), name="cart"),
    path("cart/add/<int:pk>/", AddToCartView.as_view(), name="add_to_cart"),
    path(
        "cart/update/<int:pk>/", UpdateCartItemView.as_view(), name="update_cart_item"
    ),
    path(
        "cart/delete/<int:pk>/", DeleteCartItemView.as_view(), name="delete_cart_item"
    ),
]
