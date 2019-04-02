from rest_framework import serializers
from . models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields= '__all__'



class UserUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'age']


