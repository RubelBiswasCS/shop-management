from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    ListView,
    DetailView
)
from .models import Product


def home(request):
    products = Product.objects.all()
    #template = loader.get_template('polls/index.html')
    context = {
        'products': products,
    }
    return render(request,'store/home.html',context)

class ProductListView(ListView):
    model = Product
    template_name = 'store/home.html' #<app>/<model>_<viewtype>.html
    context_object_name =  'products'
