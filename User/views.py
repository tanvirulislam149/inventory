from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet
from User.serializers import MyGroupSerializer, MyPermissionSerializer
from django.contrib.auth.models import Group, Permission

# Create your views here.
User = get_user_model()

class MyGroupViewset(ModelViewSet): 
    queryset = Group.objects.all()
    serializer_class = MyGroupSerializer

class MyPermissionViewset(ModelViewSet): 
    queryset = Permission.objects.all()
    serializer_class = MyPermissionSerializer