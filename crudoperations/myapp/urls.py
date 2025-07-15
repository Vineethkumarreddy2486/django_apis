from django.urls import path
from .views import *


urlpatterns=[
    path('products/',product_list_create,name='products'),
    path('productoperations/<int:id>/',product_operations,name='operations')
]