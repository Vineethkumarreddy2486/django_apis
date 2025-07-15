from rest_framework import serializers
from .models import *
from django.contrib.auth.hashers import make_password

class registeraSerializer(serializers.ModelSerializer):
    cnfrmPassword=serializers.CharField(write_only=True)
    class Meta:
        model = Student
        fields="__all__"
        extra_kwargs ={
            'password':{'write_only':True}
        }

    def validate(self,data):
        password=data.get('password')
        cnfrm=data.get('cnfrmPassword')
        if password != cnfrm:
            raise serializers.ValidationError('passwords do not match')
        return data
    
    def create(self,validate_data):
        validate_data.pop('cnfrmPassword')
        validate_data['password']=make_password(validate_data['password'])
        return Student.objects.create(**validate_data)
    

class loginSerializer(serializers.Serializer):
    email=serializers.EmailField()
    password=serializers.CharField(write_only=True)



# performing CRUD operations

class competetionsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Competetions
        fields='__all__'
        