from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter

# for viewsets
router=DefaultRouter()
router.register(r'competetions',competetionViewset)

urlpatterns=[
    path('register/',registration_api),
    path('login/',login_api),
    path('',include(router.urls))
]