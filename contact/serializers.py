from rest_framework import serializers
from .models import *

class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields='__all__'
    # class Meta:
    #     models=ContactMessage
    #     fields='__all__'
    
