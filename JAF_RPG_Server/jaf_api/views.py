from rest_framework import generics
from .serializers import UserSerializer
from .models import *


# Create your views here.
class UserList(generics.listCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all().order_by('user_id')
    serializer_class = UserSerializer