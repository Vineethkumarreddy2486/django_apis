from rest_framework import serializers
from .models import *
from django.contrib.auth.hashers import make_password

# Registration
class registeraSerializer(serializers.ModelSerializer):
    cnfrmPassword=serializers.CharField(write_only=True)
    class Meta:
        model = Student
        fields="__all__"
        extra_kwargs ={
            'password':{'write_only':True}
        }
    # validates the password
    def validate(self,data):
        password=data.get('password')
        cnfrm=data.get('cnfrmPassword')
        if password != cnfrm:
            raise serializers.ValidationError('passwords do not match')
        return data
    
    # creates user after registration
    def create(self,validate_data):
        validate_data.pop('cnfrmPassword')
        validate_data['password']=make_password(validate_data['password'])    #hashes the password
        return Student.objects.create(**validate_data)
    
# Login
class loginSerializer(serializers.Serializer):
    email=serializers.EmailField()
    password=serializers.CharField(write_only=True)



# performing CRUD operations
class competetionsSerializer(serializers.ModelSerializer):
    image = serializers.FileField(max_length=None, use_url=True)      # it will return the full URL of image
    class Meta:
        model=Competetions
        fields='__all__'

    def update(self, instance, validated_data):
        # Only update image if a new one is provided
        image = validated_data.get('image', None)
        if image:
            instance.image = image

        # Update other fields
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.startDate = validated_data.get('startDate', instance.startDate)
        instance.endDate = validated_data.get('endDate', instance.endDate)
        instance.status = validated_data.get('status', instance.status)
        instance.save()

        return instance
        # lookup_field="slug"
        