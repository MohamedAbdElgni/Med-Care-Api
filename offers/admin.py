from django.contrib import admin
from .models import Offer

@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = ('id', 'doctor', 'specialization', 'original_price', 'discount_price', 'created_at')
    list_filter = ('created_at', 'specialization')



