from rest_framework import serializers

from doctors.serializers import DoctorSerializer
from .models import *
from users.serializers import UserSerializer


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ['id', 'doctor', 'day', 'start_time', 'end_time', 'is_active']


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['id','doctor', 'schedule', 'user', 'create_at', 'is_accepted', 'status', 'payment_status', 'payment_method', 'payment_transaction_id', 'payment_amount']


class GetAppointmentSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    
    class Meta:
        model = Appointment
        fields = ['id','user','doctor', 'schedule', 'is_accepted', 'create_at', 'status', 'payment_status', 'payment_method', 'payment_transaction_id', 'payment_amount']

    def create(self, validated_data):
        return Appointment.objects.create(**validated_data)
    
class GetAppointmentForUserSerializer(serializers.ModelSerializer):
    doctor = DoctorSerializer()
    schedule = ScheduleSerializer()
    class Meta:
        model = Appointment
        fields = ['id','user','doctor', 'schedule', 'is_accepted', 'create_at', 'status', 'payment_status', 'payment_method', 'payment_transaction_id', 'payment_amount']

    def create(self, validated_data):
        return Appointment.objects.create(**validated_data)