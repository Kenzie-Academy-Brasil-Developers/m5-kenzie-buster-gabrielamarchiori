from django.shortcuts import render
from rest_framework.views import APIView, Request, Response, status
from rest_framework.response import Response
from .serializers import UserSerializer, CustomJWTSerializer
from .models import User
from rest_framework_simplejwt.views import TokenObtainPairView


class LoginView(TokenObtainPairView):
    serializer_class = CustomJWTSerializer


class UserView(APIView):
    def post(self, request: Request) -> Response:
        
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)
    
    def get(self, request) -> Response:
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status.HTTP_200_OK)
