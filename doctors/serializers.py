from rest_framework import serializers
from .models import *
from users.serializers import UserSerializer

class SpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialization
        fields = '__all__'

class DoctorSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    class Meta:
        model = Doctor
        fields = '__all__' 
    def create(self, validated_data):
        return Doctor.objects.create(**validated_data)  
    
    def update(self, instance, validated_data):
        user_data = validated_data.pop('user', None)
        if user_data:
            user_serializer = UserSerializer(instance.user, data=user_data)
            if user_serializer.is_valid():
                user = user_serializer.save()
                instance.user = user
            else:
                raise serializers.ValidationError(user_serializer.errors)
        instance.specialization = validated_data.get('specialization', instance.specialization)
        instance.bio = validated_data.get('bio', instance.bio)
        instance.degree = validated_data.get('degree', instance.degree)
        instance.area = validated_data.get('area', instance.area)
        instance.fees = validated_data.get('fees', instance.fees)
        instance.save()
        return instance
    
