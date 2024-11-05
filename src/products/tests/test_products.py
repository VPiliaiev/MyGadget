from django.test import TestCase

from products.models import Product, ProductCategory, ProductImage


class ProductCategoryTestCase(TestCase):
    def setUp(self):
        self.category = ProductCategory.objects.create(
            name="Electronics", description="Category for electronic products"
        )

    def test_category_creation(self):
        self.assertEqual(self.category.name, "Electronics")
        self.assertEqual(self.category.description, "Category for electronic products")
        self.assertEqual(str(self.category), "Electronics")


class ProductTestCase(TestCase):
    def setUp(self):
        self.category = ProductCategory.objects.create(name="Electronics")
        self.product = Product.objects.create(
            name="Smartphone",
            description="A smartphone with 4GB RAM",
            price=30000,
            stock=100,
            category=self.category,
        )

    def test_product_creation(self):
        self.assertEqual(self.product.name, "Smartphone")
        self.assertEqual(self.product.description, "A smartphone with 4GB RAM")
        self.assertEqual(self.product.price, 30000)
        self.assertEqual(self.product.stock, 100)
        self.assertEqual(self.product.category, self.category)
        self.assertEqual(str(self.product), "Smartphone")


class ProductImageTestCase(TestCase):
    def setUp(self):
        self.category = ProductCategory.objects.create(name="Electronics")
        self.product = Product.objects.create(
            name="Smartphone",
            description="A smartphone with 4GB RAM",
            price=30000,
            stock=100,
            category=self.category,
        )
        self.product_image = ProductImage.objects.create(
            product=self.product,
            image="product_images/smartphone.png",
            alt_text="Smartphone image",
        )

    def test_product_image_creation(self):
        self.assertEqual(self.product_image.product, self.product)
        self.assertEqual(self.product_image.image, "product_images/smartphone.png")
        self.assertEqual(self.product_image.alt_text, "Smartphone image")
        self.assertEqual(str(self.product_image), "Image for Smartphone")
