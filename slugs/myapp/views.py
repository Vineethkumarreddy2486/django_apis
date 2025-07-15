from django.shortcuts import render
from .serializers import *
from rest_framework import viewsets
from rest_framework.decorators import api_view,permission_classes
# Create your views here.

class slugViewset(viewsets.ModelViewSet):
    queryset=Slug.objects.all()
    serializer_class=slugSerializer
    lookup_field='slug'               #this tells DRF to add title in the URL

    
