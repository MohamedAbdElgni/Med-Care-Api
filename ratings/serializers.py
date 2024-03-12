from rest_framework import serializers
from .models import *

 #rating       
class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['id', 'doctor', 'user', 'rating', 'comment', 'created_at']
