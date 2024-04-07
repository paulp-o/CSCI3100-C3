from django.shortcuts import render

# Create your views here.

# Contains the views for user registration, login, and logout.
# Utilize Django's authentication system or extend it with Django Rest Framework for API views.

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import status, views, permissions, response
from rest_framework.authtoken.models import Token
from .serializers import UserSerializer


class RegisterView(views.APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(views.APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return response.Response({'token': token.key}, status=status.HTTP_200_OK)
        return response.Response(status=status.HTTP_401_UNAUTHORIZED)


class LogoutView(views.APIView):
    def post(self, request):
        request.auth.delete()
        return response.Response(status=status.HTTP_204_NO_CONTENT)


class DeleteUserView(views.APIView):
    def post(self, request):
        request.user.delete()
        return response.Response(status=status.HTTP_204_NO_CONTENT)
