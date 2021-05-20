from django.contrib import admin
from .models import Product,Order,OrderItem
#all models are register here.
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)