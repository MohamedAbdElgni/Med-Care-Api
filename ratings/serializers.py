from rest_framework import serializers

from users.serializers import UserSerializer
from .models import *
from users.models import User

 #rating       
class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['id','user','doctor', 'rating', 'comment', 'created_at']
    def create(self, validated_data):
        return Rating.objects.create(**validated_data)  
    




class DoctorRatings(serializers.ModelSerializer):
    """
    this to get the patent obj with each rating 
    """
    user = UserSerializer()
    class Meta:
        model = Rating
        fields = ['id','user','doctor', 'rating', 'comment', 'created_at']
    def create(self, validated_data):
        return Rating.objects.create(**validated_data)