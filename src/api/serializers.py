from rest_framework.serializers import ModelSerializer

from mygadget.models import (CartItem, Comparison, Order, Product,
                             ProductCategory, Wishlist)


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name", "description", "price", "stock", "category"]


class ProductCategorySerializer(ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ["id", "name", "description"]


class CartItemSerializer(ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = CartItem
        fields = ["id", "customer", "product", "quantity", "is_active"]


class WishlistSerializer(ModelSerializer):
    class Meta:
        model = Wishlist
        fields = ["id", "customer", "product", "added_at"]
        read_only_fields = ["added_at"]


class ComparisonSerializer(ModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = Comparison
        fields = ["id", "customer", "products", "created_at"]


class OrderSerializer(ModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = Order
        fields = [
            "id",
            "customer",
            "products",
            "order_date",
            "total_amount",
            "is_active",
        ]
