from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Product
from .forms import NameForm
from django.contrib.auth.decorators import login_required


def home(request):
    products = Product.objects.all()
    #template = loader.get_template('polls/index.html')
    context = {
        'products': products,
    }
    return render(request,'store/all_products.html',context)


def delete_product(request):

    products = Product.objects.all()
   
    context = {
        'products': products,
    }
    return render(request,'store/delete_product_view.html',context)   
def confirm_delete_view(request, pk):
    # dictionary for initial data with 
    # field names as keys
    
   
    
  
    # fetch the object related to passed id
    obj = get_object_or_404(Product, pk = pk)
    context = {
       'product': obj 
    }
  
  
    if request.method =="POST":
        # delete object
        obj.delete()
        # after deleting redirect to 
        # home page
        return HttpResponseRedirect('/delete_product')
  
    return render(request, "confirm_delete_product.html", context)


def add_product(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            product_code = form.cleaned_data['product_code']
            name = form.cleaned_data['name']
            category = form.cleaned_data['category']
            unit_price = form.cleaned_data['unit_price']
            current_stock = form.cleaned_data['current_stock']
            
            p = Product(product_code=product_code,
            name=name,category=category,unit_price=unit_price,
            current_stock=current_stock)
            p.save()
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'store/add_product.html', {'form': form})

def update_product(request):
    products = Product.objects.all()
   
    context = {
        'products': products,
    }
    return render(request,'store/update_product_view.html',context)   

def update_product_view(request, pk):
    
    # if this is a POST request we need to process the form data
    
    obj = get_object_or_404(Product, pk = pk)
    initial_dict={
        'product_code' : obj.product_code,
        'name' : obj.name,
        'category': obj.category,
        'unit_price' : obj.unit_price,
        'current_stock' : obj.current_stock
        }
    # create a form instance and populate it with data from the request:

    form = NameForm(request.POST or None, initial = initial_dict)
    # check whether it's valid:
    
    if form.is_valid():
        # process the data in form.cleaned_data as required
        product_code = form.cleaned_data['product_code']
        name = form.cleaned_data['name']
        category = form.cleaned_data['category']
        unit_price = form.cleaned_data['unit_price']
        current_stock = form.cleaned_data['current_stock']

        
       
        Product.objects.filter(pk=pk).update(
        product_code=product_code,
        name=name,
        category=category,
        unit_price=unit_price,
        current_stock=current_stock
    )

        
        # ...
        # redirect to a new URL:
        return HttpResponseRedirect('/update_product/')

    # if a GET (or any other method) we'll create a blank form
    
    
        

    return render(request, 'store/update_product_form.html', {'form': form})

def manage_product(request):
    products = Product.objects.all()
    #template = loader.get_template('polls/index.html')
    context = {
        'products': products,
    }
    return render(request,'store/manage_product.html',context)

def added_product(request):
    products = Product.objects.all()
    #template = loader.get_template('polls/index.html')
    context = {
        'products': products,
    }
    return render(request,'store/added_product.html',context)          