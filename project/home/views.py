from django.shortcuts import render
from rest_framework.views import APIView
from . models import UserModel
from . serializer import RegisterSerializer,loginSerializer
from rest_framework.response import Response
from rest_framework import status
from . token import get_tokens_for_user
from django.contrib.auth.hashers import make_password
from rest_framework.exceptions import AuthenticationFailed

# Create your views here.


class register(APIView):
    def post(self,request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data":serializer.data,"messege":"register successfull"})
        return Response({"messege":"somthing wrong"})
    

class Userlogin(APIView):
    
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = UserModel.objects.filter(email=email).first()
        if user is None:
            raise AuthenticationFailed('User Not Found!')
        if not user.check_password(password):
            raise AuthenticationFailed('invalid password! or mail')
        if user:
            token = get_tokens_for_user(user)

        return Response({"token":token,"messege":"login success full"})

        
class UserProfile(APIView):
    def post(self,request):
        pass