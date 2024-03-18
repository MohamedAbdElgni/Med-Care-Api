from rest_framework import serializers
from .models import *
from users.serializers import UserSerializer


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ['id', 'doctor', 'day', 'start_time', 'end_time', 'is_active']


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['id','doctor', 'schedule', 'user', 'create_at', 'is_accepted']


class GetAppointmentSerializer(serializers.ModelSerializer):
    """
    this to get the patent obj with each appointmetn
    """
    user = UserSerializer()
    class Meta:
        model = Appointment
        fields = ['id','user','doctor', 'schedule', 'is_accepted', 'create_at']
    def create(self, validated_data):
        return Appointment.objects.create(**validated_data)