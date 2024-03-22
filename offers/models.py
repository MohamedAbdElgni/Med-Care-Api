
from django.db import models
from doctors.models import Doctor
from datetime import datetime

class Offer(models.Model):
    DEFAULT_SPECIALIZATION = "General"  # Default specialization

    doctor = models.ForeignKey(Doctor, related_name='offers', on_delete=models.CASCADE)
    specialization = models.CharField(max_length=50, default=DEFAULT_SPECIALIZATION)  # Set default specialization
    image_url = models.ImageField(upload_to='offer_images/', default='offer_images/offer.jpg') 
    original_price = models.DecimalField(max_digits=10, decimal_places=2)  
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  
    created_at = models.DateTimeField(default=datetime.now, editable=False)

    def __str__(self):
        return f"Offer for {self.specialization} by {self.doctor} ({self.created_at})"

