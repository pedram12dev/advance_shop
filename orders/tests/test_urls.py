from django.test import TestCase
from django.urls import reverse, resolve
from orders.views import CartView, CartAddView, CartRemoveView, OrderDetailView, OrderCreateView


class TestUrls(TestCase):
    def test_cart_url(self):
        url = reverse('orders:orders_cart')
        self.assertEqual(resolve(url).func.view_class , CartView)

    def test_cart_add_url(self):
        url = reverse('orders:cart_add' , args=('1' , ))
        self.assertEqual(resolve(url).func.view_class , CartAddView)

    def test_cart_remove_url(self):
        url = reverse('orders:cart_remove' , args=('1' , ))
        self.assertEqual(resolve(url).func.view_class , CartRemoveView)

    def test_order_create_url(self):
        url = reverse('orders:orders_create')
        self.assertEqual(resolve(url).func.view_class , OrderCreateView)

    def test_order_detail_url(self):
        url = reverse('orders:order_detail' , args=('1' , ))
        self.assertEqual(resolve(url).func.view_class , OrderDetailView)