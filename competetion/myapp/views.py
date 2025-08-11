
from django.contrib.auth.hashers import check_password
from .serializers import *
from rest_framework import status,viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import api_view,permission_classes
# Create your views here.

@api_view(['POST'])
@permission_classes([AllowAny])
def registration_api(request):
        serializer=registeraSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'you have registered successfully'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([AllowAny])
def login_api(request):
        serializer = loginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password=serializer.validated_data['password'] 
            try:
                #   this compares the email
                  student=Student.objects.get(email=email)
            except Student.DoesNotExist:
                  return Response({'error':'invalid email or password'},status=status.HTTP_401_UNAUTHORIZED)
        # authenticate will works only for User(built-in) and extended User model in django
        # checkpassword() is used to compare the plain password and hashed password (from custom model)
            if check_password(password,student.password):
                #   to return user info 
                  return Response({
                        'message':'Login successful',
                        'email':student.email,
                        'lastName':student.lastName,
                        'firstName':student.firstName
                  })
            else:
                  return Response({'error':'invalid email or password'},status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)




# CRUD operations

class competetionViewset(viewsets.ModelViewSet):
      queryset=Competetions.objects.all()
      serializer_class=competetionsSerializer
      parser_classes = [MultiPartParser, FormParser]
      # lookup_field='slug'                                      #this tells DRF to add slug in URL
