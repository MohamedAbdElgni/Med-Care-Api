from rest_framework import serializers
from .models import Offer

class OfferSerializer(serializers.ModelSerializer):
    doctor_name = serializers.SerializerMethodField()

    def get_doctor_name(self, obj):
        doctor = obj.doctor
        return f"{doctor.user.first_name} {doctor.user.last_name}"

    class Meta:
        model = Offer
        fields = ['id', 'doctor', 'doctor_name', 'specialization', 'image_url', 'original_price', 'discount_price', 'created_at']

