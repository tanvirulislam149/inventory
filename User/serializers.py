from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer, UserSerializer as BaseUserSerializer
from rest_framework import serializers
from User.models import CustomUser
from django.contrib.auth.models import Group, Permission

class UserCreateSerializer(BaseUserCreateSerializer):

    class Meta(BaseUserCreateSerializer.Meta):
        fields = ["id", "email", "first_name", "last_name", "password", "address", "phone_number"]


class UserSerializer(BaseUserSerializer):
    is_staff = serializers.SerializerMethodField(method_name="get_is_staff")

    class Meta(BaseUserSerializer.Meta):
        fields = ["id", "email","first_name", "last_name", "password", "address", "phone_number", "is_staff"]
    
    def get_is_staff(self, user: CustomUser):
        return user.is_staff
    

class MyPermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = "__all__"


class MyGroupSerializer(serializers.ModelSerializer):
    permissions = MyPermissionSerializer(many=True)
    class Meta:
        model = Group
        fields = ["id", "name", "permissions"]