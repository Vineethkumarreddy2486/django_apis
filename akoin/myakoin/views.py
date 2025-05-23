# register api
from rest_framework.decorators import api_view
from .serializers import RegisterSerializer, LoginSerializer
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate

@api_view(['POST'])
def register_api(request):
    if request.method == 'POST':
        serializer= RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'you have successfully registered'},status=status.HTTP_200_OK)
    return Response(serializer.errors,status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
def login_api(request):
    if request.method == 'POST':
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username=serializer.validated_data['username']
            password=serializer.validated_data['password']
            user = authenticate(username=username,password=password)
            if user:
                return Response('Login Successful',status=status.HTTP_200_OK)
            return Response("'errors': 'Invalid credentials'",status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)