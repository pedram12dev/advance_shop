from django.test import TestCase
from products.models import Product, Category
from django.urls import reverse


class TestProductsModel(TestCase):
    def setUp(self):
        Category.objects.create(name='winter wear', slug='winter-wear')
        Product.objects.create(name='winter wear', slug='winter-wear', price=400, category_id=1)

    def test_product_get_absolute_url(self):
        product = Product.objects.get(slug='winter-wear')
        self.assertEqual(product.get_absolute_url(), reverse('products:product_detail', args=('winter-wear',)))
