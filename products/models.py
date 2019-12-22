import os
import random
from django.db import models


def get_filename_ext(filepath):
    '''
    Split the basename and extension of the uploaded filename.
    Returns name, ext
    '''
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    new_filename = random.randint(1,999999999)
    name, ext = get_filename_ext(filename)
    complete_filename = f'{new_filename}{ext}'
    return f'products/{new_filename}{complete_filename}'


class ProductManager(models.Manager):
    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id)
        if qs.count() == 1:
            return qs.first()
        return None

    def active(self):
        qs = self.get_queryset().filter(active=True)
        if qs.count() >= 1:
            return qs
        return None


class Product(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    colour = models.CharField(max_length=20, null=True)
    active = models.BooleanField(default=True)
    in_stock = models.BooleanField(default=True)
    date_updated = models.DateTimeField(auto_now=True)

    objects = ProductManager()

    def __str__(self):
        return '{}'.format(self.name)


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=upload_image_path, blank=True, null=True)
    thumbnail = models.ImageField(upload_to='product-thumbnails', null=True)


class ProductTag(models.Model):
    products = models.ManyToManyField(Product, blank=True)
    name = models.CharField(max_length=32)
    description = models.TextField(blank=True)
    active = models.BooleanField(default=True)


class Stock(models.Model):
    product_id = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)