from django.urls import path
from . import views

app_name = 'products'
urlpatterns = [
    path('', views.ProductsView.as_view(), name='v_products')
]
