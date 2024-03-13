from rest_framework import serializers

from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    def get_by_id(self, user_id):
        user = User.objects.get(id=user_id)
        return user

    def delete_by_id(self, user_id):
        user = User.objects.get(id=user_id)
        user.delete()
        return user

class DoctorSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    class Meta:
        model = Doctor
        fields = ['user', 'specialization', 'bio', 'degree']  
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
        instance.save()
        return instance
    


class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'phone', 'age', 'dob', 'address']
        extra_kwargs = {'first_name': {'required': True}, 'last_name': {'required': True}}
    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.age = validated_data.get('age', instance.age)
        instance.dob = validated_data.get('dob', instance.dob)
        instance.address = validated_data.get('address', instance.address)
        instance.save()
        return instance
    

