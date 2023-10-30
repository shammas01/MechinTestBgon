from rest_framework import serializers
from.models import UserModel



class RegisterSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UserModel
        fields = ['email','username','password']


class loginSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['email','password']
        