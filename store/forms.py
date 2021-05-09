from django import forms


class NameForm(forms.Form):
    product_code = forms.IntegerField(label='Product Code ',)
    name = forms.CharField(max_length=100)
    category = forms.CharField(max_length=100)
    unit_price = forms.FloatField()
    current_stock = forms.IntegerField()