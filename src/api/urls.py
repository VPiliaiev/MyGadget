from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from api.views import (CartItemCreateView, CartItemDeleteView,
                       CartItemListView, CartItemUpdateView,
                       ComparisonListView, OrderListView,
                       ProductCategoryCreateView, ProductCategoryDeleteView,
                       ProductCategoryDetailView, ProductCategoryListView,
                       ProductCategoryUpdateView, ProductCreateView,
                       ProductDeleteView, ProductDetailView, ProductListView,
                       ProductUpdateView, WishlistListView)

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
urlpatterns = [
    path("docs/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    path("products/", ProductListView.as_view(), name="product_list"),
    path("products/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
    path("products/create/", ProductCreateView.as_view(), name="product_create"),
    path(
        "products/<int:pk>/update/", ProductUpdateView.as_view(), name="product_update"
    ),
    path(
        "products/<int:pk>/delete/", ProductDeleteView.as_view(), name="product_delete"
    ),
    path("categories/", ProductCategoryListView.as_view(), name="category_list"),
    path(
        "categories/<int:pk>/",
        ProductCategoryDetailView.as_view(),
        name="category_detail",
    ),
    path(
        "categories/create/",
        ProductCategoryCreateView.as_view(),
        name="category_create",
    ),
    path(
        "categories/<int:pk>/update/",
        ProductCategoryUpdateView.as_view(),
        name="category_update",
    ),
    path(
        "categories/<int:pk>/delete/",
        ProductCategoryDeleteView.as_view(),
        name="category_delete",
    ),
    path("cartitems/", CartItemListView.as_view(), name="cartitem_list"),
    path("cartitems/create/", CartItemCreateView.as_view(), name="cartitem_create"),
    path(
        "cartitems/<int:pk>/update/",
        CartItemUpdateView.as_view(),
        name="cartitem_update",
    ),
    path(
        "cartitems/<int:pk>/delete/",
        CartItemDeleteView.as_view(),
        name="cartitem_delete",
    ),
    path("wishlists/", WishlistListView.as_view(), name="wishlist_list"),
    # Comparison
    path("comparisons/", ComparisonListView.as_view(), name="comparison_list"),
    path("orders/", OrderListView.as_view(), name="order_list"),
    path("auth/", include("djoser.urls.jwt")),
]
