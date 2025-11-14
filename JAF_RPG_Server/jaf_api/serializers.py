from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer): # To handle custom user_id
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['user_id'] = str(user.user_id)
        return token