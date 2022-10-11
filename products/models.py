from pydoc import describe
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length = 255)
    description = models.CharField(max_length = 255)
    price = models.DecimalField(max_digits = 9, decimal_places = 2)
    
    