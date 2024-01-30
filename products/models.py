from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('products:category' , args=[self.slug , ])


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='c_products')
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=50, unique=True)
    image = models.ImageField()
    available = models.BooleanField(default=False)
    description = models.TextField()
    price = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('products:product_detail' , args=[self.slug , ])
