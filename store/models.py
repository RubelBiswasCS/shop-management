from django.db import models
from django.urls import reverse



class Product(models.Model):
    #product code, name, category, unit price, current stock
    product_code = models.IntegerField(unique=True)
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    unit_price = models.FloatField()
    current_stock = models.IntegerField()
    
    def __str__(self):
        return self.name


class Order(models.Model):
    #customer name, phone and email.
    order_id = models.IntegerField(unique=True)
    customer_name =  models.CharField(max_length=100)
    phone = models.CharField(max_length=14)
    email = models.EmailField()

    def __str__(self):
        return self.customer_name