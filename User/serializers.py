from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer, UserSerializer as BaseUserSerializer
from rest_framework import serializers
from User.models import CustomUser
from django.contrib.auth.models import Group, Permission

class UserCreateSerializer(BaseUserCreateSerializer):

    class Meta(BaseUserCreateSerializer.Meta):
        fields = ["id", "email", "first_name", "last_name", "password", "address", "phone_number"]

class SimpleGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ["id", "name"]

class UserSerializer(BaseUserSerializer):
    groups = SimpleGroupSerializer(many=True, read_only=True)

    class Meta(BaseUserSerializer.Meta):
        fields = ["id", "email","first_name", "last_name", "password", "address", "phone_number", "groups"]


class CreateMyGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ["id", "name", "permissions"]


class MyPermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = "__all__"

class MyGroupSerializer(serializers.ModelSerializer):
    permissions = MyPermissionSerializer(many=True)
    class Meta:
        model = Group
        fields = ["id", "name", "permissions"]