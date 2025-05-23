from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework import response

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    email = serializers.EmailField(required=True)
    cnfrm_password = serializers.CharField(write_only=True)


    class Meta:
        model=User
        fields=['username','email','password','cnfrm_password']

    def validate(self,data):
        if data['password'] != data['cnfrm_password']:
            raise serializers.ValidationError ("passwords must match")
        return data
    
    # creating the user
    def create(self,validated_data):
        validated_data.pop('cnfrm_password')
        password=validated_data.pop('password')
        # create_user hashes the password automatically before saving in database 
        user=User(**validated_data)
        user.set_password(password)
        user.save()
        return user
    
    # or


    # def create(self,validated_data):
    #     validated_data.pop('cnfrm_password')
    #     user=User.objects.create_user(**validated_data)
    #     return user



class LoginSerializer(serializers.Serializer):
    username=serializers.CharField(max_length=60)
    password=serializers.CharField(min_length=8,write_only=True)