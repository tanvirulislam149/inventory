from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet
from User.serializers import MyGroupSerializer, MyPermissionSerializer, CreateMyGroupSerializer, UserSerializer
from django.contrib.auth.models import Group, Permission
from Core.permissions import IsOwner
from djoser.views import UserViewSet
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
User = get_user_model()

class MyGroupViewset(ModelViewSet): 
    queryset = Group.objects.all()
    permission_classes = [IsOwner]
    
    def get_serializer_class(self):
        if self.request.method in ["POST", "PUT", "PATCH"]:
            return CreateMyGroupSerializer
        else:
            return MyGroupSerializer

class MyPermissionViewset(ModelViewSet): 
    http_method_names = ["get", "head", "options"]
    queryset = Permission.objects.all()
    serializer_class = MyPermissionSerializer
    permission_classes = [IsOwner]


class CustomUserViewset(UserViewSet):
    @action(detail=True, methods=["patch"], permission_classes=[IsOwner])
    def assign_role(self, request, *args, **kwargs):
        user = self.get_object()
        role = request.data.get("role")  # demo data ==> {"role": "Staff"}

        if not role:
            raise ValidationError({"role": "Please enter role."})
        
        user.groups.clear()
        group = Group.objects.get(name=role)
        user.groups.add(group)

        return Response(
            {
                "message": f"User '{user.email}' role changed to '{role}'.",
                "role": role,
            },
            status=status.HTTP_200_OK,
        )
        
        