from django.shortcuts import render
from rest_framework import generics
from .serializers import *
class RegisterView(generics.GenericAPIView):
    serilazer_class = RegisterSerializer
    def post(self,request):
        user = request.data
        serializer = self.serilazer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

# Create your views here.
