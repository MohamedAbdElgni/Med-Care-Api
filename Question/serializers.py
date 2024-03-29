from rest_framework import serializers
from .models import UserQuestion

class UserQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserQuestion
        fields = ['id', 'user', 'question', 'created_at']

