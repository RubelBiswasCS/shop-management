from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
from django.shortcuts import render,redirect, get_object_or_404
from .models import Product,Order,OrderItem
from .forms import OrderForm,ProductForm,ItemSelectForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .utils import render_to_pdf
from num2words import num2words
import datetime
from django.core import serializers
from django.core import serializers


#view of delete proudct
@login_required
def delete_product(request):

    products = Product.objects.all()
   
    context = {
        'products': products,
    }
    return render(request,'store/delete_product_view.html',context)

#vidw for confirming deletion of product    
@login_required
def confirm_delete_view(request, pk):

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
        return HttpResponseRedirect('/delete_product')
  
    return render(request, "confirm_delete_product.html", context)

#view for adding product
@login_required
def add_product(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance 
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
            return redirect('add-product')
            #return HttpResponseRedirect('')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ProductForm()

    return render(request,'store/add_product.html', {'form': form})

#all instace of Product model passed to all_product template as context dictonary"
@login_required
def all_product(request):
    products = Product.objects.all()
    #template = loader.get_template('polls/index.html')
    context = {
        'products': products,
    }
    return render(request,'store/all_products.html',context) 
    
#all product list with 'update prodoct' action 
@login_required
def update_product(request):
    products = Product.objects.all()
   
    context = {
        'products': products,
    }
    return render(request,'store/update_product_view.html',context)   

#update selected product 
@login_required
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

        #update product with current value
        Product.objects.filter(pk=pk).update(
        product_code=product_code,
        name=name,
        category=category,
        unit_price=unit_price,
        current_stock=current_stock
    )


        # redirect to a new URL:
        return HttpResponseRedirect('/update_product/')        

    return render(request, 'store/update_product_form.html', {'form': form})

#manage product view
@login_required
def manage_product(request):
    products = Product.objects.all()
    
    context = {
        'products': products,
    }
    return render(request,'store/manage_product.html',context)
  

@login_required
def manage_order(request):
    orders = Order.objects.all()
    #template = loader.get_template('polls/index.html')
    context = {
        'orders': orders,
    }
    return render(request,'store/view_order.html',context) 


#view for creating order
@login_required
def create_order(request):
    

    if request.method == 'POST':
        
        # create a form instance 
        form_o = OrderForm(request.POST)
        

        # check whether it's valid:
        if form_o.is_valid():
            # process the data in form.cleaned_data as required
            customer_name = form_o.cleaned_data['customer_name']
            phone = form_o.cleaned_data['phone']
            email = form_o.cleaned_data['email']
            
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

    
    return render(request,'store/create_order.html',{'form_o': form_o,})     

@login_required
def add_to_cart(request,pk):
    order = Order.objects.get(pk=pk)#get_object_or_404(Order, pk = pk) #

    initial_dict = {
        'product' : "Select Item", 
        'qty' : 1
    }
    
    
    form_i = ItemSelectForm(request.POST or None,initial=initial_dict)
    context = {
    'order': order,
    'form_i' : form_i,
    
    }

    if 'cancle' in request.POST:
        OrderItem.objects.filter(order__order_id=order.order_id).delete()
        order.delete()
        return HttpResponseRedirect(reverse('create-order'))
    elif 'checkout' in request.POST:
        order.date_n_time = datetime.datetime.now()
        order.save()
        items = OrderItem.objects.filter(order__order_id=order.order_id)
        for item in items:
            #assigning the updated current_stock value to each ordered product
            item.product.current_stock -= item.qty
            item.product.save()

        return HttpResponseRedirect(reverse('create-invoice', kwargs={'pk': order.pk}))
    else:
        pass
    
    # else:
    #     if form_i.is_valid():

    #     # process the data in form.cleaned_data as required 
        
    #         qty = form_i.cleaned_data['qty']
    #         product = form_i.cleaned_data['product']
            
    #         if product.current_stock >= qty:

                

    #             if not OrderItem.objects.filter(order__order_id=order.order_id,
    #                 product__product_code=product.product_code).exists():
                    
    #                 o_i = OrderItem(product=product,order = order, qty=qty)
    #                 o_i.save()
    #             else:
    #                 c_oi=OrderItem.objects.get(order__order_id=order.order_id,
    #                 product__product_code=product.product_code)
                    
    #                 OrderItem.objects.filter(order__order_id=order.order_id,
    #                 product__product_code=product.product_code).update(qty=qty)

            #current_ordered_items = OrderItem.objects.filter(order__order_id=order.order_id)
            #return HttpResponseRedirect(reverse('add-to-cart',kwargs={'pk':pk}))
            
            #return JsonResponse({"c_o_i":list(current_ordered_items.values())})   
        
        # orderItem = OrderItem.objects.filter(order__order_id=order.order_id)
        # total = sum(item.get_total for item in orderItem)
        context = {
                'order': order,
                'form_i' : form_i,
                # 'orderItem' : orderItem,
                # 'total' : total,
                }
        return render(request,'store/cart.html',context)
def cart_form(request):
    if request.method == "POST":

        
        qty = request.POST.get('qty')
        pk = request.POST.get('product')
        product = Product.objects.get(pk=pk)
        
        order_id = request.POST.get('order_id')
        order = Order.objects.get(order_id=order_id)
        
        if product.current_stock >= int(qty):


            if not OrderItem.objects.filter(order__order_id=order_id,
                product__product_code=product.product_code).exists():
                
                o_i = OrderItem(product=product,order = order, qty=qty)
                o_i.save()
            else:
                c_oi=OrderItem.objects.get(order__order_id=order.order_id,
                product__product_code=product.product_code)
                
                OrderItem.objects.filter(order__order_id=order.order_id,
                product__product_code=product.product_code).update(qty=qty)
            #response = "Item added to cart"
        else:
            response = "insufficent stock"
       
    return HttpResponse(response)
def current_cart(request):
    order_id = request.POST.get('order_id')
    current_ordered_items = OrderItem.objects.filter(order__order_id=order_id).values('product__name','product__unit_price','qty')
    
    
    return JsonResponse({"c_o_i":list(current_ordered_items),})
    


#detail view for order
@login_required
def order_detail_view(request,pk):
    order = Order.objects.get(pk=pk)
  
    orderItem = OrderItem.objects.filter(order__order_id=order.order_id)
    total = sum(item.get_total for item in orderItem)
    context = {
        'order': order,
        'orderItem' : orderItem,
        'total' : total,
    }
    return render(request,'store/order_details.html',context)

#view for creating invoice
@login_required
def create_invoice(request,pk):
    order = Order.objects.get(pk=pk)
    orderItem = OrderItem.objects.filter(order__order_id=order.order_id)
    total = sum(item.get_total for item in orderItem)
    total_in_words = num2words(total)
    data = {    
        'order': order,
        'orderItem' : orderItem,
        'total' : total,
        'total_in_words' : total_in_words,
        }
    pdf = render_to_pdf('store/invoice_pdf.html', data)
    if pdf:
        return HttpResponse(pdf, content_type='application/pdf')
    return HttpResponse("Not Found")    
   