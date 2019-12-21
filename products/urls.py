from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('list/', views.ProductListView.as_view(), name='list'),
    path('product/<pk>', views.ProductDetailView.as_view(), name='product'),
]