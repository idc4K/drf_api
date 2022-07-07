from rest_framework import serializers
from .models import User

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=68,min_length=8,write_only=True)
    first_name = serializers.CharField(max_length=120)
    last_name = serializers.CharField(max_length=120)
    
    class Meta:
        model = User
        fields = ['last_name','first_name','email','password']

    
    def validate(self,attrs):
        email = attrs.get('email','')
        first_name = attrs.get('first_name','')
        last_name = attrs.get('last_name','')

        if not first_name.isalnum():
            if not last_name.isalnum():
                serializers.ValidationError("first_name and last_name should only contain alpha numeric character")
                
        return attrs

    def create(self,validated_data):
        return User.objects.create_user(**validated_data)