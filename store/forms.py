from django import forms
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
