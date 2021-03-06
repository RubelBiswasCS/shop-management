from django.urls import path

from . import views
from .views import create_order

urlpatterns = [
   
    path('home/',views.create_order,name='store-home'),
    path('',views.create_order,name='store-home'),
    path('manage_product/',views.all_product,name='manage-product'),
    path('add_product/',views.add_product,name='add-product'),
    path('all_products/',views.all_product,name='all-products'),
    path('update_product/',views.update_product,name='update-product'),
    path('delete_product/',views.delete_product,name='delete-product'),
    path('<int:pk>/delete_product/', views.confirm_delete_view, name='confirm-delete-view'),
    path('<int:pk>/update_product/', views.update_product_view, name='update-product-view'),

    path('manage_order/',views.manage_order,name='manage-order'),
    path('create_order/',views.create_order,name='create-order'),
    path('view_order/',views.manage_order,name='view-order'),
    path('<int:pk>/add_to_cart/', views.add_to_cart, name='add-to-cart'),

    path('current_cart/', views.current_cart, name='current-cart'),
    path('cart_form/', views.cart_form, name='cart-form'),    

    path('<int:pk>/order_details/', views.order_detail_view, name='order-detail-view'),
    path('<int:pk>/invoice/', views.create_invoice, name='create-invoice'),

]