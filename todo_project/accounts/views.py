from django.shortcuts import render

# Create your views here.
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserRegistrationSerializer

@api_view(['POST'])
def register_user(request):
    if request.method == 'POST':
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Create the user
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
