from django.db import models
from django.contrib.auth.models import User

class Address(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    postcode = models.CharField(max_length=10)
    house_number = models.CharField('Number', max_length=35)
    street = models.CharField(max_length=50)
    town = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.postcode} - {self.house_number}'