from rest_framework import serializers
from .models import *


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ['id', 'doctor', 'day', 'start_time', 'end_time', 'is_active']


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['id','doctor', 'schedule', 'user', 'create_at', 'is_accepted']
