from rest_framework import serializers
from .models import User
from rest_framework.validators import UniqueValidator


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(
        validators=[UniqueValidator(queryset=User.objects.all(), message="username already taken.")]
    )
    email = serializers.EmailField(
        max_length=127,
        validators=[UniqueValidator(queryset=User.objects.all(), message="email already registered.")]
    )
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    password = serializers.CharField(write_only=True)
    birthdate = serializers.DateField(required=False)
    is_employee = serializers.BooleanField(required=False)
    is_superuser = serializers.BooleanField(read_only=True)

    def create(self, validated_data: dict) -> User:
        if 'is_employee' in validated_data.keys():
            if validated_data['is_employee'] is True:
                validated_data['is_superuser'] = True
        
        return User.objects.create_user(**validated_data)
