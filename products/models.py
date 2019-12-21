from django.db import models

# Create your models here.
class Product(models.Model):
    title       = models.CharField(max_length=128)
    description = models.TextField(null=True)
    price       = models.DecimalField(max_digits=8, decimal_places=2)
    colour      = models.CharField(max_length=20, null=True)

    def __str__(self):
        return '{}'.format(self.title)