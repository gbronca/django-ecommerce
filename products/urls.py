from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.ProductListView.as_view(), name='products_list'),
    path('<pk>', views.ProductDetailView.as_view(), name='product_detail'),
]