from django.shortcuts import render
from rest_framework import generics,status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User
from .serializers import *
class RegisterView(generics.GenericAPIView):
    serilazer_class = RegisterSerializer
    def post(self,request):
        user = request.data
        serializer = self.serilazer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        
        user = User.objects.get(email=user_data['email'])
        token = RefreshToken.for_user(user)

        return Response(user_data, status=status.HTTP_201_CREATED)

# Create your views here.
