from rest_framework import serializers
from .models import *

class slugSerializer(serializers.ModelSerializer):
    class Meta:
        model=Slug
        fields="__all__"
        extra_kwargs={
            'slug':{'read_only':True}
        }