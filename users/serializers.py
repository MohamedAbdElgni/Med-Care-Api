from rest_framework import serializers

from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'is_patient', 'is_doctor', 'phone', 'age', 'dob', 'address', 'city', 'gender', 'password','first_name','last_name']
        extra_kwargs = {'password': {'write_only': True}}
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        if password:
            user.set_password(password)
        user.save()
        return user

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['user', 'specialization', 'bio', 'degree']  

    def create(self, validated_data):
        return Doctor.objects.create(**validated_data)
            
