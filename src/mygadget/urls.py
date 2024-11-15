from django.urls import path

from mygadget.views import CartItemView, ProductDetailView, ProductListView

urlpatterns = [
    path("", ProductListView.as_view(), name="product_list"),
    path("<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
    path("cart/", CartItemView.as_view(), name="cart_items"),
]
