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


    