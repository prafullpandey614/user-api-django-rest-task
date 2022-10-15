from msilib.schema import Feature
from rest_framework import serializers
from .models import User, FriendShip

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = '__all__'

class FriendShipSerializer(serializers.ModelSerializer):
    class Meta:
        model = FriendShip
        exclude = ['date']
        # fields = '__all__'
        