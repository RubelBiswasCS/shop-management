from django.db import models
from django.urls import reverse
import random

def unique_order_id():
    not_unique = True
    while not_unique:
        uo_id = random.randint(1000000000, 9999999999)
        if not Order.objects.filter(order_id=uo_id):
            not_unique = False
    return uo_id


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
    order_id = models.IntegerField(unique=True, 
                        default=unique_order_id)
    customer_name =  models.CharField(max_length=100)
    phone = models.CharField(max_length=14)
    email = models.EmailField()

    p_name = models.CharField(max_length=200,default="")
    
    def __str__(self):
        return self.customer_name

    


