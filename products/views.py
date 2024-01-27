from django.shortcuts import render , get_object_or_404
from django.views import View
from .models import Product


class ProductsView(View):
    def get(self, request):
        products = Product.objects.all()
        return render(request , 'products/products.html' , {'products':products})


class ProductDetailView(View):
    def get(self , request , slug):
        product = get_object_or_404(Product , slug=slug)
        return render(request , 'products/products_detail.html' , {'product':product})