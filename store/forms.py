from django import forms
from .models import Product
import random


class ProductForm(forms.Form):
    product_code = forms.IntegerField(label='Product Code ',)
    name = forms.CharField(max_length=100)
    category = forms.CharField(max_length=100)
    unit_price = forms.FloatField()
    current_stock = forms.IntegerField()

class OrderForm(forms.Form):
    #order_id = forms.IntegerField()
    customer_name =  forms.CharField(max_length=100)
    phone = forms.CharField(max_length=14)
    email = forms.EmailField()
    #p_name = forms.ChoiceField(label='Select Product',choices=list ((obj.product_code,obj.name) for obj in Product.objects.all()))

class ItemSelectForm(forms.Form):
    p_name = forms.ChoiceField(label='Select Product',choices=list ((obj.product_code,obj.name) for obj in Product.objects.all()))    