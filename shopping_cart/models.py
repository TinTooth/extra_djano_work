
from django.db import models
from customers.models import Customer
from products.models import Product

# Create your models here.
class ShoppingCart(models.Model):
    customer = models.ForeignKey(Customer, on_delete = models.CASCADE)
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    quantity = models.IntegerField(default = 0)

