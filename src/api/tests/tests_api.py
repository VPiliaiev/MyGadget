from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from mygadget.models import Product, ProductCategory


class ProductAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.category = ProductCategory.objects.create(name="Electronics")
        self.product = Product.objects.create(
            name="Test Product",
            description="Description of product",
            price=100,
            stock=10,
            category=self.category,
        )
        self.list_url = reverse("product_list")
        self.detail_url = reverse("product_detail", kwargs={"pk": self.product.pk})
        self.create_url = reverse("product_create")
        self.update_url = reverse("product_update", kwargs={"pk": self.product.pk})
        self.delete_url = reverse("product_delete", kwargs={"pk": self.product.pk})

        self.user = get_user_model().objects.create_user(email="user@example.com", password="qwerty1234")
        self.client.force_authenticate(user=self.user)

    def test_list_products(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 1)
        self.assertEqual(response.json()[0]["name"], self.product.name)

    def test_get_product_detail(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()["name"], self.product.name)

    def test_create_product(self):
        data = {
            "name": "New Product",
            "description": "New Description",
            "price": "200",
            "stock": 5,
            "category": self.category.id,
        }
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 2)
        self.assertEqual(Product.objects.last().name, "New Product")

    def test_update_product(self):
        data = {
            "name": "Updated Product",
            "description": "Updated Description",
            "price": "300",
            "stock": 15,
            "category": self.category.id,
        }
        response = self.client.put(self.update_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.product.refresh_from_db()
        self.assertEqual(self.product.name, "Updated Product")

    def test_delete_product(self):
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Product.objects.count(), 0)
