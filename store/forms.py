from django import forms
from .models import Product
import random
from django.core.exceptions import ValidationError

#form for adding product
class ProductForm(forms.Form):
    product_code = forms.IntegerField(label='Product Code ',)
    name = forms.CharField(max_length=100)
    category = forms.CharField(max_length=100)
    unit_price = forms.FloatField()
    current_stock = forms.IntegerField()

#form for order information
class OrderForm(forms.Form):
    
    customer_name =  forms.CharField(max_length=100)
    phone = forms.CharField(max_length=14)
    email = forms.EmailField()
    
#form for adding item form dropdown menu and quantity from int field
class ItemSelectForm(forms.Form):
    #p_name = forms.ChoiceField(label='Select Product',choices=list ((obj.product_code,obj.name) for obj in Product.objects.all()))   
    product = forms.ModelChoiceField(Product.objects.all(), label='Select Product', empty_label="Select")
    qty = forms.IntegerField()

    #function for checking product avaiability
    def clean_qty(self):
        data = self.cleaned_data['qty']
        #product_code = self.cleaned_data['p_name']
        product = self.cleaned_data['product']
        if data > product.current_stock:
            raise forms.ValidationError(('Insufficient Stock'), code='ins_stock')
        # Always return a value to use as the new cleaned data, even if
        # this method didn't change it.
        return data
    