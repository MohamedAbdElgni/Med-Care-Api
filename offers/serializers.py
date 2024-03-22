from rest_framework import serializers
from .models import Offer

class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = ['id', 'doctor', 'specialization', 'image_url', 'original_price', 'discount_price', 'created_at']

