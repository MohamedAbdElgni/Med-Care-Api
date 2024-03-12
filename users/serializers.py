from rest_framework import serializers

from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'is_patient', 'is_doctor', 'phone', 'age', 'dob', 'address', 'city', 'gender']
        
    def create(self, validated_data):
        return User.objects.create(**validated_data)

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['user', 'specialization', 'bio', 'degree']  

    def create(self, validated_data):
        return Doctor.objects.create(**validated_data)
