from django.db import models
from django.urls import reverse
import random

import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw


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

    qr_code = models.ImageField(upload_to='qr_codes', blank=True)

    #products = models.ManyToManyField(OrderItem)
    
    #p_name = models.CharField(max_length=200,default="")
    
    def __str__(self):
        return self.customer_name

    def save(self, *args, **kwargs):
        qr_info = "Invoice No : "+ str(self.order_id)+" Name : "+self.customer_name +" Phone : "+str(self.phone)+ " Email : "+ self.email
        qrcode_img = qrcode.make(qr_info)
        #canvas = Image.new('RGB', (290, 290), 'white')
        canvas = Image.new('RGB', (qrcode_img.pixel_size, qrcode_img.pixel_size), 'white')
        canvas.paste(qrcode_img)
        fname = f'qr_code-{self.customer_name}.png'
        buffer = BytesIO()
        canvas.save(buffer,'PNG')
        self.qr_code.save(fname, File(buffer), save=False)
        canvas.close()
        super().save(*args, **kwargs)

class OrderItem(models.Model):
    
    qty = models.IntegerField(default=0)

    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)

    @property
    def get_total(self):
        total = self.product.unit_price * self.qty
        return total

    
    #p_name = models.CharField(max_length=200,default="")
    #qr_info = 'Invoice No : '+ str(self.order_id)+'Name : '+self.customer_name+ +'Phone : '+str(self.phone)+ 'Email :'+ self.email
