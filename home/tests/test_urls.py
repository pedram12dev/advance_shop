from django.test import SimpleTestCase
from django.urls import reverse , resolve
from home.views import HomeView , BucketHome


class TestUrls(SimpleTestCase):
    def test_home(self):
        url = reverse('home:home')
        self.assertEqual(resolve(url).func.view_class , HomeView)

    def test_bucket_home(self):
        url = reverse('home:bucket')
        self.assertEqual(resolve(url).func.view_class , BucketHome)