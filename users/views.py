from django.shortcuts import render
from rest_framework.views import APIView, Request, Response, status
from rest_framework.response import Response
from .serializers import UserSerializer


class UserView(APIView):
    def post(self, request: Request) -> Response:
        
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)
