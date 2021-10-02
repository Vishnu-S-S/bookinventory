from rest_framework import serializers
from .models import *


class LoginSerializer(serializers.ModelSerializer):
    """Login serializer for user login."""

    class Meta:
        model = User
        fields = ('email', 'password')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'username')


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'username', 'password')
