from django.db import models
from users.models import *
from doctors.models import *

# Create your models here.
class Schedule(models.Model):
    weekday_choices = (
        ('saturday', 'Saturday'),
        ('sunday', 'Sunday'),
        ('monday', 'Monday'),
        ('tuesday', 'Tuesday'),
        ('wednesday', 'Wednesday'),
        ('thursday', 'Thursday'),
        ('friday', 'Friday'),
    )
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    day = models.CharField(max_length=9, choices=weekday_choices)
    start_time = models.TimeField(null=False)
    end_time = models.TimeField(null=False)
    is_active = models.BooleanField(default=True)


class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    is_accepted = models.BooleanField(default=False)
    status = models.CharField(max_length=20, choices=[("pending", "Pending"), ("accepted", "Accepted"), ("rejected", "Rejected"), ("completed", "Completed")], default="pending")
    payment_status = models.CharField(max_length=20, choices=[("pending", "Pending"), ("paid", "Paid"), ("failed", "Failed")], default="pending")
    payment_method = models.CharField(max_length=50, blank=True, null=True)
    payment_transaction_id = models.CharField(max_length=100, blank=True, null=True)
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
