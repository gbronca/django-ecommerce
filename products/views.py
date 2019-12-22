from django.shortcuts import render, get_object_or_404, Http404
from django.views.generic import ListView, DetailView
from .models import Product

class ProductListView(ListView):
    template_name = 'products/products.html'

    def get_queryset(self, *args, **kwargs):
        return Product.objects.active()


class ProductDetailView(DetailView):
    # queryset = Product.objects.all()
    template_name = 'products/product.html'

    def get_context_data(self, *args, **kwargs):
        return super(ProductDetailView, self).get_context_data(*args, **kwargs)

    def get_object(self, *args, **kwargs):
        request = self.request
        pk = self.kwargs.get('pk')
        instance = Product.objects.get_by_id(pk)
        if instance is None:
            raise Http404("Product doesn't exist")
        return instance