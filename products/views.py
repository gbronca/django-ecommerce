from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product
# Create your views here.

class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = 'products/list.html'


class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    template_name = 'products/product.html'