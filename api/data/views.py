from django.shortcuts import render
from rest_framework import generics,status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .utils import Util
from .models import User
from .serializers import *
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
class RegisterView(generics.GenericAPIView):
    serilazer_class = RegisterSerializer
    def post(self,request):
        user = request.data
        serializer = self.serilazer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        
        user = User.objects.get(email=user_data['email'])
        token = RefreshToken.for_user(user).access

        current_site = get_current_site(request)
        relativeLink = reverse('verifyEmail')
        data = {'domain':current_site}
        absurl = 'http://'+current_site+relativeLink+"?token="+token.access
        Util.send_email(data)
        return Response(user_data, status=status.HTTP_201_CREATED)



class VerifyEmail(generics.GenericAPIView):
    def get(self):
        pass 
# Create your views here.
