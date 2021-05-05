from django.urls import path
from .views import (
    ProductListView
)
from . import views

urlpatterns = [
   
    path('home/',ProductListView.as_view(),name='store-home'),
    path('',ProductListView.as_view(),name='store-home'),
]