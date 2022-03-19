from pyexpat import model
from django.db import models

# Create your models here.
class Club(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    symbol = models.CharField(max_length=10)


    def __str__(self):
        return self.symbol