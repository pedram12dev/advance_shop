from django.shortcuts import render
from django.views import View
from products.models import Product
from .tasks import all_bucket_objects_task

class HomeView(View):
    def get(self , request):
        products = Product.objects.filter(available = True)
        return render (request , 'home/index.html' , {'products':products})


class BucketHome(View):
    template_name = 'home/bucket.html'
    def get(self , request):
        objects = all_bucket_objects_task()
        return render (request , self.template_name , {'objects':objects})