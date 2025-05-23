from django.urls import path
from .views import *
urlpatterns=[
    path('register/',register_api,name="register"),
    path('login/',login_api,name="login")
]