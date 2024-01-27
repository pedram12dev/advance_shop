from django.shortcuts import render
from django.views import View


class ProductsView(View):
    def get(self, request):
        return render(request , 'products/products.html')
