from django.test import TestCase
from django.urls import reverse, resolve
from products.views import ProductsView, ProductDetailView


class TestUrls(TestCase):
    def test_product_url(self):
        url = reverse('products:v_products')
        self.assertEqual(resolve(url).func.view_class, ProductsView)

    def test_product_category_url(self):
        url = reverse('products:category', args=('winter-wear',))
        self.assertEqual(resolve(url).func.view_class, ProductsView)

    def test_product_detail_url(self):
        url = reverse('products:product_detail', args=('winter-slug',))
        self.assertEqual(resolve(url).func.view_class, ProductDetailView)
