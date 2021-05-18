from django import forms
from .models import Product
import random
from django.core.exceptions import ValidationError

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
    qty = forms.IntegerField()


    def clean_qty(self):
        data = self.cleaned_data['qty']
        if data > 4:
             raise ValidationError(
                    "Did not send for 'help' in the subject despite "
                    "CC'ing yourself."
                )
        # Always return a value to use as the new cleaned data, even if
        # this method didn't change it.
        return data