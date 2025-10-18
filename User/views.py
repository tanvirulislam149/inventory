from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet
from User.serializers import MyGroupSerializer, MyPermissionSerializer, CreateMyGroupSerializer
from django.contrib.auth.models import Group, Permission

# Create your views here.
User = get_user_model()

class MyGroupViewset(ModelViewSet): 
    queryset = Group.objects.all()
    
    def get_serializer_class(self):
        if self.request.method in ["POST", "PUT", "PATCH"]:
            return CreateMyGroupSerializer
        else:
            return MyGroupSerializer

class MyPermissionViewset(ModelViewSet): 
    queryset = Permission.objects.all()
    serializer_class = MyPermissionSerializer