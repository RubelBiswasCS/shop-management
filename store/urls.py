from django.urls import path
from .views import (
    ProductListView
)
from . import views

urlpatterns = [
   
    path('home/',views.get_name,name='store-home'),
    path('',ProductListView.as_view(),name='store-home'),
]