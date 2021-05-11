from django.urls import path
from .views import (
    ProductListView
)
from . import views

urlpatterns = [
   
    path('home/',views.home,name='store-home'),
    path('',views.home,name='store-home'),
    path('manage_product/',views.manage_product,name='manage-product'),
    path('add_product/',views.add_product,name='add-product'),
    path('all_products/',views.home,name='all-products'),
]