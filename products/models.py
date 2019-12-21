from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    colour = models.CharField(max_length=20, null=True)
    image = models.FileField(upload_to='products/')

    def __str__(self):
        return '{}'.format(self.title)


class Stock(models.Model):
    product_id = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)