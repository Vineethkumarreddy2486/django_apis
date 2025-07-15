from rest_framework import serializers
from django.core.exceptions import ValidationError 
import re
def validate_name(value):
    if not re.fullmatch(r'[A-Za-z]+', value):
        raise serializers.ValidationError("name should not contain any special characters and digits")
    

def validate_college(value):
    if len(value.strip())<5:
        raise ValidationError ('college name should contain alteast 5 characters')
    
    if not re.fullmatch(r'[A-Za-z ]+',value):
        raise ValidationError("college name should not contain any special characters and digits")
    
def validate_phone(value):
    if not re.fullmatch(r'\d{10}',value):
        raise ValidationError('phone number should contain exactly 10 digits')
    

def validate_strong_password(value):
    if len(value.strip())<8:
        raise ValidationError('password should contain atleast 8 characters')
    if not re.search(r"[A-Z]",value):
        raise ValidationError('password should contain atleast 1 uppercase')
    if not re.search(r"[a-z]",value):
        raise ValidationError('password should contain atleast 1 lowercase')
    if not re.search(r"[0-9]",value):
        raise ValidationError('passwprd should contain atleast 1 digit')
    if not re.search(r"[!@#$%^&*()_+=\-{}\[\]:;\"'<>,.?/]",value):
        raise ValidationError('password should contain atleast 1 special character')