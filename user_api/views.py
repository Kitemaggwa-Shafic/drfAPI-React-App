from django.shortcuts import render
from django.contrib.auth.models import get_user_model, login, logout
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserRegisterSerializer, UserSerializer, UserLoginSerializer
from rest_framework import permissions, status

# Create your views here.

class UserRegister(APIView):
    permission_classes =(permissions.AllowAny)
    def post(self, request):
        clean_data = custom_validation(request.data)
        serializer = UserRegisterSerializer(data=clean_data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.create_user(clean_data)
            if user:
                return Response(serializer.data, status=status.HTTP_200_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
class UserLogin(APIView):
    pass

class UserLogout(APIView):
    pass

class UserView(APIView):
    pass