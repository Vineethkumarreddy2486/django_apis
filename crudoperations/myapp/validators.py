from rest_framework import serializers
def only_positive(value):
    if value<0:
        raise serializers.ValidationError('price must be positive')
    return value