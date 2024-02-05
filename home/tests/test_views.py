from django.test import TestCase, Client
from products.models import Product, Category
from django.urls import reverse
from model_bakery import baker
from django.core.files.uploadedfile import SimpleUploadedFile
from home.tasks import all_bucket_objects_task


class TestHomeView(TestCase):
    def setUp(self):
        self.client = Client()
        Category.objects.create(name='test category', slug='test-category')
        self.product = baker.make(Product, available=True,
                                  image=SimpleUploadedFile('winter wear_320x320.jpg', b"file_content",
                                                           content_type='image/jpeg'))

    def test_home_view_GET(self):
        Product.objects.get(available=True)
        response = self.client.get(reverse('home:home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')
        self.failUnless(response.context['products'])

    def test_bucket_home_GET(self):
        all_bucket_objects_task()
        response = self.client.get(reverse('home:bucket'))
        self.assertEqual(response.status_code , 200)
        self.assertTemplateUsed(response , 'home/bucket.html')
        self.failUnless(response.context['objects'])