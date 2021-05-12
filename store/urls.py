from django.urls import path
from .views import (
    ProductListView
)
from . import views

urlpatterns = [
   
    path('home/',views.home,name='store-home'),
    path('',views.home,name='store-home'),
    path('manage_product/',views.home,name='manage-product'),
    path('add_product/',views.add_product,name='add-product'),
    path('all_products/',views.home,name='all-products'),
    path('update_product/',views.update_product,name='update-product'),
    path('delete_product/',views.delete_product,name='delete-product'),
    path('<int:product_code>/delete_product/', views.confirm_delete_view, name='confirm-delete-view'),
    path('<int:product_code>/update_product/', views.update_product_view, name='update-product-view'),
]