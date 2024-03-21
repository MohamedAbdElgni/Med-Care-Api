from django.db import models
from doctors.models import Doctor
from datetime import datetime

class Offer(models.Model):
    doctor = models.ForeignKey(Doctor, related_name='offers', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(default=datetime.now, editable=False)

    def __str__(self):
        return self.title

