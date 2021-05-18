from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Product,Order
from .forms import OrderForm,ProductForm,ItemSelectForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse



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
        form = ProductForm(request.POST)
        
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
        form = ProductForm()

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

    form = ProductForm(request.POST or None, initial = initial_dict)
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



def manage_order(request):
    orders = Order.objects.all()
    #template = loader.get_template('polls/index.html')
    context = {
        'orders': orders,
    }
    return render(request,'store/view_order.html',context) 

def create_order(request):
    

    if request.method == 'POST':
        
        # create a form instance and populate it with data from the request:
        form_o = OrderForm(request.POST)
        
        # check whether it's valid:
        if form_o.is_valid():
            # process the data in form.cleaned_data as required
            #order_id = form_o.cleaned_data['order_id']
            customer_name = form_o.cleaned_data['customer_name']
            phone = form_o.cleaned_data['phone']
            email = form_o.cleaned_data['email']
            #p_name = form_o.cleaned_data['p_name']
            #order_id=order_id, into order
            
            p = Order(
            customer_name=customer_name,phone=phone,email=email)
            p.save()
            pk = p.pk
            # ...
            # redirect to a new URL:kwargs={'app_label': 'auth'}
            return HttpResponseRedirect(reverse('add-to-cart', kwargs={'pk':pk}))

    # if a GET (or any other method) we'll create a blank form
    else:
        form_o = OrderForm()
        #return HttpResponseRedirect(reverse('/add_to_cart/', kwargs={'pk':'pk'}))

    
    return render(request,'store/create_order.html',{'form_o': form_o,})     


def add_to_cart(request,pk):
    order = Order.objects.get(pk=pk)#get_object_or_404(Order, pk = pk) #
    #template = loader.get_template('polls/index.html')
    form_i = ItemSelectForm(request.POST)
    

    if form_i.is_valid():
        # process the data in form.cleaned_data as required
        
        product_code = form_i.cleaned_data['p_name']

        product = Product.objects.get(product_code = product_code)
        
        
        order.products.add(product)
        #Order.objects.filter(pk=pk).update(
        #p_name=all_item)
    

    # if a GET (or any other method) we'll create a blank form
    p = order.products.all()
    context = {
        'order': order,
        'form_i' : form_i,
        'p' : p
    }

    
    return render(request,'store/cart.html',context)     